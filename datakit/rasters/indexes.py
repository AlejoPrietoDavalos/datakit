""" TODO: Ordenar los indices por temática o uso."""
__all__ = ["ndvi"]
from .typings import BandArr
import numpy as np


def safe_divide(numerator: np.ndarray, denominator: np.ndarray, default_value=0) -> np.ndarray:
    with np.errstate(divide='ignore', invalid='ignore'):
        result = np.divide(numerator, denominator)
        result[~np.isfinite(result)] = default_value
    return result


def ndvi(red: BandArr, nir: BandArr) -> BandArr:
    """ Normalized Difference Vegetation Index."""
    return safe_divide(nir - red, nir + red)

def ndwi(nir: BandArr, swir: BandArr) -> BandArr:
    """ Normalized Difference Water Index."""
    return safe_divide(nir - swir, nir + swir)

def ndbi(nir: BandArr, swir: BandArr) -> BandArr:
    """ Normalized Difference Built-up Index."""
    return safe_divide(swir - nir, swir + nir)

def ndmi(nir: BandArr, swir: BandArr) -> BandArr:
    """ Normalized Difference Moisture Index."""
    return safe_divide(nir - swir, nir + swir)

def savi(nir: BandArr, red: BandArr, L=0.5) -> BandArr:
    """ Soil-Adjusted Vegetation Index."""
    assert 0<=L<=1
    return (1 + L) * safe_divide(nir - red, nir + red + L)

def evi(nir: BandArr, red: BandArr, blue: BandArr, L=1, C1=6, C2=7.5, G=2.5) -> BandArr:
    """ Enhanced Vegetation Index.
    - TODO: Revisar esos hiperparámetros."""
    return G * safe_divide(nir - red, nir + C1 * red - C2 * blue + L)

def mndwi(green: BandArr, swir: BandArr) -> BandArr:
    """ Modified Normalized Difference Water Index."""
    return safe_divide(green - swir, green + swir)

def bai(nir: BandArr, swir: BandArr) -> BandArr:
    """ Burned Area Index."""
    ###return (1 / ((0.1 - nir) ** 2 + (0.06 - swir) ** 2)) ** 0.5
    raise NotImplementedError("Buscar bien este indice.")
