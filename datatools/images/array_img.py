__all__ = ["ArrayImg"]

from datatools.images.abc import AbstractImg
from datatools.validators import assert_ndarray_2D

from pydantic import field_validator

import numpy as np


class ArrayImg(AbstractImg):
    arr: np.ndarray

    @property
    def height(self) -> int:
        return self.arr.shape[0]
    
    @property
    def width(self) -> int:
        return self.arr.shape[1]

    @field_validator("arr")
    def _validate_arr(cls, arr: np.ndarray):
        assert_ndarray_2D(arr)
        return arr
