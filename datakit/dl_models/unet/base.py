""" U-NET Model, semantic segmentation. https://arxiv.org/pdf/1505.04597.pdf"""
from torch import Tensor, nn
import torch.nn.functional as F

from datakit.dl_models.utils import iter_pairs_chann
from datakit.dl_models.unet.config import UNETConfig
from datakit.dl_models.some_layers import (
    Conv2DParams, MaxPool2dParams,
    DoubleConvPool, DoubleConvUpsampling,
    DoubleConv, conv2d
)

from typing import List, Tuple


def get_unet_encoder(
        n_channels: List[int],
        p_conv2d: Conv2DParams,
        p_pool: MaxPool2dParams) -> nn.ModuleList:
    """ Encoder de la UNET."""
    encoder = nn.ModuleList()

    for in_channels, out_channels in iter_pairs_chann(n_channels):
        double_conv_pool = DoubleConvPool(
            in_channels = in_channels,
            out_channels = out_channels,
            p_conv2d = p_conv2d,
            p_pool = p_pool
        )
        encoder.append(double_conv_pool)
    return encoder

def get_unet_decoder(
        n_channels: List[int],
        p_conv2d: Conv2DParams,
        up_conv_stride = 2,
        up_conv_padding = 0) -> nn.ModuleList:
    
    decoder = nn.ModuleList()
    for in_channels, out_channels in iter_pairs_chann(n_channels):
        double_conv_up = DoubleConvUpsampling(
            in_channels = in_channels,
            out_channels = out_channels,
            p_conv2d = p_conv2d,
            up_conv_stride = up_conv_stride,
            up_conv_padding = up_conv_padding
        )
        decoder.append(double_conv_up)

    return decoder


class EncoderUNET(nn.Module):
    def __init__(self, cfg: UNETConfig, p_conv2d: Conv2DParams, p_pool: MaxPool2dParams):
        super().__init__()
        self.e_modules = get_unet_encoder(cfg.encoder_channels, p_conv2d, p_pool)

    def forward(self, t: Tensor) -> Tuple[Tensor, List[Tensor]]:
        residuals: List[Tensor] = []
        for e_module in self.e_modules:
            t, r = e_module(t)
            residuals.append(r)
        return t, residuals


class DecoderUNET(nn.Module):
    def __init__(self, cfg: UNETConfig, p_conv2d: Conv2DParams, asd_1, asd_2):
        super().__init__()
        self.d_modules = get_unet_decoder(cfg.decoder_channels, p_conv2d, asd_1, asd_2)

    def forward(self, t: Tensor, residuals: List[Tensor], dim) -> Tensor:
        for i, d_module in enumerate(self.d_modules):
            i_res = len(residuals) - (i+1)
            t = d_module.forward(t, residuals[i_res], dim)
        return t


class BaseUNET(nn.Module):
    def __init__(self, cfg: UNETConfig, p_conv2d: Conv2DParams, p_pool: MaxPool2dParams):
        super().__init__()
        self.encoder = EncoderUNET(cfg, p_conv2d, p_pool)
        self.double_conv = DoubleConv(cfg.encoder_channels[-1], cfg.botton_channel, p_conv2d)
        self.decoder = DecoderUNET(cfg, p_conv2d, 2, 0)
        self.out_conv = conv2d(cfg.decoder_channels[-1], cfg.n_bands_out, p_conv2d)

    def forward(self, t: Tensor, dim=1) -> Tensor:
        assert len(t.shape) == 4, "`shape: [n_imgs x n_channels x HEIGHT x WIDTH]`"
        #----------Encoder----------
        t, residuals = self.encoder.forward(t)
        
        #----------Botton----------
        t = self.double_conv.forward(t)

        #----------Decoder----------
        t = self.decoder.forward(t, residuals, dim)
        
        #----------Head----------
        t = self.out_conv.forward(t)
        t = F.softmax(t, dim=dim)   # Conviene dejarlo afuera?
        return t

#    @torch.no_grad()
#    def predict(self, x: Tensor) -> Tensor:
#        x = self(x)
#        x = torch.argmax(x, 1, keepdim = True)
#        return x