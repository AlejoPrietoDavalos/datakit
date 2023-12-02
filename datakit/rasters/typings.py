""" Typing para datos raster."""
__all__ = ["BandArr", "RGBArr"]
import numpy as np

from typing import NewType

BandArr = NewType("band_arr", np.ndarray)
RGBArr = NewType("RGB_arr", np.ndarray)