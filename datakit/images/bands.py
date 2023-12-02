""" FIXME: Ver si se puede desacoplar el @field_validator y hacerlo genérico."""
__all__ = ["BandsRGB", "BandsRGBNir"]
from datakit.pydantic_base import BaseModelValAssign
from datakit.validators import assert_ndarray_2D
from datakit.rasters import RGBArr
from datakit import T_NDArray

from abc import ABC

import numpy as np
from pydantic import field_validator

_RGB_BANDS = ("red", "green", "blue")


class BandsRGB(BaseModelValAssign):
    """ TODO: Poner condicional de len(shape)==2."""
    red: T_NDArray
    green: T_NDArray
    blue: T_NDArray

    @property
    def rgb(self) -> RGBArr:
        """ Array 3D con las bandas stackeadas."""
        return np.stack([self.red, self.green, self.blue], axis=-1)

    @field_validator(*_RGB_BANDS)
    def _val_bands(cls, arr: np.ndarray) -> np.ndarray:
        assert_ndarray_2D(arr)
        return arr


class BandsRGBNir(BandsRGB):
    """ TODO: Todo lo que se puede calcular con estas bandas."""
    nir: T_NDArray

    @field_validator(*_RGB_BANDS, "nir")
    def _val_bands(cls, arr: np.ndarray) -> np.ndarray:
        assert_ndarray_2D(arr)
        return arr
