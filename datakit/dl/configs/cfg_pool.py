from datakit.dl.configs.cfg_module import CfgModuleDumpable
from datakit.dl.common_types import _size_any_t

from torch import nn
from typing import Type, Optional

__all__ = ["CfgMaxPool2d"]

class CfgMaxPool2d(CfgModuleDumpable):
    kernel_size: _size_any_t
    stride: Optional[_size_any_t] = None
    padding: _size_any_t = 0
    dilation: _size_any_t = 1
    return_indices: bool = False
    ceil_mode: bool = False

    @property
    def module_cls(self) -> Type[nn.MaxPool2d]:
        return nn.MaxPool2d

