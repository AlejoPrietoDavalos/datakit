from .cfg_module import CfgModuleDumpable
from torch import nn

from typing import Type

class CfgBatchNorm2d(CfgModuleDumpable):
    num_features: int
    eps: float = 1e-5
    momentum: float = 0.1
    affine: bool = True
    track_running_stats: bool = True

    @property
    def module_cls(self) -> Type[nn.BatchNorm2d]:
        return nn.BatchNorm2d
