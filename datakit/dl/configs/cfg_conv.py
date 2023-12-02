from datakit.dl.configs import CfgModuleBase

from torch.nn.common_types import _size_2_t
from pydantic import NonNegativeInt


class CfgConv2d(CfgModuleBase):
    in_channels: NonNegativeInt
    out_channels: NonNegativeInt
    kernel_size: _size_2_t
    stride: _size_2_t = 1
    padding: _size_2_t | str = 0
    dilation: _size_2_t = 1
    groups: int = 1
    bias: bool = True
    padding_mode: str = 'zeros'



