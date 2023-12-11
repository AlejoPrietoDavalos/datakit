from datakit.gis.indexes.common_calcs import safe_divide, norm_diff_index

import numpy as np
from numpy import ndarray

__all__ = ["ndvi", "gndvi", "savi", "msavi", "evi", "gari", "gvmi", "ndgi", "arvi"]

def ndvi(nir: ndarray, red: ndarray) -> ndarray:
    """ Normalized Difference Vegetation Index (NDVI)."""
    return norm_diff_index(nir, red)

def gndvi(nir: ndarray, green: ndarray) -> ndarray:
    """ Green Normalized Difference Vegetation Index (GNDVI)."""
    return norm_diff_index(nir, green)

def savi(nir: ndarray, red: ndarray, L=0.5) -> ndarray:
    """ Soil-Adjusted Vegetation Index (SAVI)."""
    assert 0<=L<=1
    return (1 + L) * safe_divide(nir - red, nir + red + L)

def msavi(nir: ndarray, red: ndarray) -> ndarray:
    """ Modified Soil Adjusted Vegetation Index (MSAVI)."""
    return 0.5 * (2 * (nir + 1) - np.sqrt((2 * nir + 1)**2 - 8 * (nir - red)))

def evi(nir: ndarray, red: ndarray, blue: ndarray, L=1, C1=6, C2=7.5, G=2.5) -> ndarray:
    """ Enhanced Vegetation Index (EVI)."""
    return G * safe_divide(nir - red, nir + C1 * red - C2 * blue + L)

def gari(nir: ndarray, green: ndarray, red: ndarray, blue: ndarray) -> ndarray:
    """ Green Atmospherically Resistant Index (GARI)."""
    return norm_diff_index(nir, green - (blue - red))

def gvmi(nir: ndarray, swir2: ndarray) -> ndarray:
    """ Global Vegetation Moisture Index (GVMI)."""
    return safe_divide((nir + 0.1) - (swir2 + 0.02), (nir + 0.1) + (swir2 + 0.02))

def ndgi(green: ndarray, nir: ndarray) -> ndarray:
    """ Normalized Difference Greenness Index (NDGI)."""
    return norm_diff_index(green, nir)

def arvi(nir: ndarray, red: ndarray, blue: ndarray) -> ndarray:
    """ Atmospherically Resistant Vegetation Index (ARVI)."""
    return norm_diff_index(nir, 2 * red - blue)

