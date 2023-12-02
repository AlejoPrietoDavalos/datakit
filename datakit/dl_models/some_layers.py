import torch
from torch import Tensor, nn
import torch.nn.functional as F

from pydantic import BaseModel, Field

from typing import Tuple


class Conv2DParams(BaseModel):
    kernel_size: int = Field(frozen=True, default=3)
    stride: int = Field(frozen=True, default=1)
    padding: int = Field(frozen=True, default=1)

class MaxPool2dParams(BaseModel):
    kernel_size: int = Field(frozen=True, default=2)
    stride: int = Field(frozen=True, default=2)


def conv2d(in_channels: int, out_channels: int, p_conv2d: Conv2DParams) -> nn.Conv2d:
    """ Retorna un layer `nn.Conv2D`."""
    return nn.Conv2d(in_channels, out_channels, **p_conv2d.model_dump())


class DoubleConv(nn.Module):
    """
    FIXME: Poner relu variable.
    TODO: Hacer una "bateria" de Convs y que este sea un caso concreto de n_convs=2.
    """
    def __init__(self, in_channels: int, out_channels: int, p_conv2d: Conv2DParams):
        super().__init__()
        # TODO: Meter esto en un nn.ModuleList
        self.conv_1 = conv2d(in_channels, out_channels, p_conv2d)
        self.bn_1 = nn.BatchNorm2d(out_channels)
        self.conv_2 = conv2d(out_channels, out_channels, p_conv2d)
        self.bn_2 = nn.BatchNorm2d(out_channels)
    
    def forward(self, x: Tensor) -> Tensor:
        x = self.conv_1.forward(x)
        x = self.bn_1.forward(x)
        x = F.relu(x)

        x = self.conv_2.forward(x)
        x = self.bn_2.forward(x)
        x = F.relu(x)
        return x


class DoubleConvPool(nn.Module):
    def __init__(
            self,
            in_channels: int,
            out_channels: int,
            p_conv2d: Conv2DParams,
            p_pool: MaxPool2dParams):
        super().__init__()

        self.double_conv = DoubleConv(in_channels, out_channels, p_conv2d)
        self.max_pool = nn.MaxPool2d(**p_pool.model_dump())

    def forward(self, x: Tensor) -> Tuple[Tensor, Tensor]:
        residual = self.double_conv.forward(x)
        x = self.max_pool.forward(residual)
        return x, residual


class DoubleConvUpsampling(nn.Module):
    def __init__(
            self,
            in_channels: int,
            out_channels: int,
            p_conv2d: Conv2DParams,
            up_conv_stride = 2,
            up_conv_padding = 0):
        super().__init__()
        
        self.up_conv = nn.ConvTranspose2d(
            in_channels,
            out_channels,
            kernel_size = 2,
            stride = up_conv_stride,
            padding = up_conv_padding # FIXME, mejorar esto.
        )
        self.double_conv = DoubleConv(in_channels, out_channels, p_conv2d)
    
    def forward(self, t: Tensor, residual: Tensor, dim=1) -> Tensor:
        t = self.up_conv.forward(t)
        t = torch.cat([t, residual], dim=dim)
        t = self.double_conv.forward(t)
        return t

