from datatools.dl.configs import CfgModuleBase

from datatools.dl.common_types import _size_2_t


class CfgConv2d(CfgModuleBase):
    in_channels: int
    out_channels: int
    kernel_size: _size_2_t
    stride: _size_2_t = 1
    padding: _size_2_t | str = 0
    dilation: _size_2_t = 1
    groups: int = 1
    bias: bool = True
    padding_mode: str = 'zeros'



