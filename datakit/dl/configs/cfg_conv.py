from .cfg_module import CfgModuleDumpable

from torch.nn.common_types import _size_2_t
from pydantic import NonNegativeInt

__all__ = ["CfgConv2d"]

class CfgConv2d(CfgModuleDumpable):
    in_channels: NonNegativeInt
    out_channels: NonNegativeInt
    kernel_size: _size_2_t
    stride: _size_2_t = 1
    padding: _size_2_t | str = NonNegativeInt
    dilation: _size_2_t = 1
    groups: int = 1
    bias: bool = True
    padding_mode: str = 'zeros'


class CfgConv2dNorm:
    pass


