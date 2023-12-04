from .cfg_module import CfgModuleDumpable
from torch import nn

from pydantic import NonNegativeInt, PositiveFloat
from typing import Type

__all__ = ["CfgBatchNorm2d"]

class CfgBatchNorm2d(CfgModuleDumpable):
    num_features: NonNegativeInt
    eps: PositiveFloat = 1e-5
    momentum: PositiveFloat = 0.1
    affine: bool = True
    track_running_stats: bool = True

    @property
    def module_cls(self) -> Type[nn.BatchNorm2d]:
        return nn.BatchNorm2d
