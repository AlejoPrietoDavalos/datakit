from .cfg_module import CfgModuleDumpable

from torch import nn

from pydantic import NonNegativeInt
from datakit.dl.common_types import _size_2_t
from typing import Type


__all__ = ["CfgConv2d"]


from enum import StrEnum, auto
class PaddingMode(StrEnum):
    """ TODO: Testear"""
    zeros = auto()
    reflect = auto()
    replicate = auto()
    circular = auto()

    @classmethod
    def default(cls) -> str:
        return cls.zeros.value


class CfgConv2d(CfgModuleDumpable):
    in_channels: NonNegativeInt
    out_channels: NonNegativeInt
    kernel_size: _size_2_t
    stride: _size_2_t = 1
    padding: _size_2_t | str = 0
    dilation: _size_2_t = 1
    groups: NonNegativeInt = 1
    bias: bool = True
    padding_mode: PaddingMode = PaddingMode.default()

    @property
    def module_cls(self) -> Type[nn.Conv2d]:
        return nn.Conv2d


class CfgConvTranspose2d(CfgModuleDumpable):
    in_channels: NonNegativeInt
    out_channels: NonNegativeInt
    kernel_size: _size_2_t
    stride: _size_2_t = 1
    padding: _size_2_t = 0
    output_padding: _size_2_t = 0
    groups: NonNegativeInt = 1
    bias: bool = True
    dilation: _size_2_t = 1
    padding_mode: PaddingMode = PaddingMode.default()

    @property
    def module(self) -> Type[nn.ConvTranspose2d]:
        return nn.ConvTranspose2d

