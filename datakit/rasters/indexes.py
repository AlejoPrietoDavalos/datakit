""" TODO: Ordenar los indices por temática o uso."""
__all__ = ["ndvi"]
from .typings import BandArr
import numpy as np

from typing import Callable, Tuple

def wrapper_div_zero(fn_calc_index: Callable[[np.ndarray], np.ndarray]) -> Callable:
    def wrapper(*args, **kwargs):
        with np.errstate(divide='ignore', invalid='ignore'):
            index_arr = fn_calc_index(*args, **kwargs)
            index_arr[~np.isfinite(index_arr)] = 0
        return index_arr
    return wrapper

@wrapper_div_zero
def ndvi(red: BandArr, nir: BandArr) -> BandArr:
    """ Normalized Difference Vegetation Index."""
    ndvi_arr = (nir - red) / (nir + red)
    return ndvi_arr

@wrapper_div_zero
def ndwi(nir: BandArr, swir: BandArr) -> BandArr:
    """ Normalized Difference Water Index."""
    return (nir - swir) / (nir + swir)

@wrapper_div_zero
def ndbi(nir: BandArr, swir: BandArr) -> BandArr:
    """ Normalized Difference Built-up Index."""
    return (swir - nir) / (swir + nir)

@wrapper_div_zero
def ndmi(nir: BandArr, swir: BandArr) -> BandArr:
    """ Normalized Difference Moisture Index."""
    return (nir - swir) / (nir + swir)

@wrapper_div_zero
def savi(nir: BandArr, red: BandArr, L=0.5) -> BandArr:
    """ Soil-Adjusted Vegetation Index."""
    assert 0<=L<=1
    return ((nir - red) / (nir + red + L)) * (1 + L)

@wrapper_div_zero
def evi(nir: BandArr, red: BandArr, blue: BandArr, L=1, C1=6, C2=7.5, G=2.5) -> BandArr:
    """ Enhanced Vegetation Index.
    - TODO: Revisar esos hiperparámetros."""
    return G * ((nir - red) / (nir + C1 * red - C2 * blue + L))

@wrapper_div_zero
def mndwi(green: BandArr, swir: BandArr) -> BandArr:
    """ Modified Normalized Difference Water Index."""
    return (green - swir) / (green + swir)

@wrapper_div_zero
def bai(nir: BandArr, swir: BandArr) -> BandArr:
    """ Burned Area Index."""
    #return (1 / ((0.1 - nir) ** 2 + (0.06 - swir) ** 2)) ** 0.5
    raise NotImplementedError("Buscar bien este indice.")
