"""
- TODO: Ordenar los indices por temática o uso.
- TODO: Agregas"""
__all__ = ["ndvi"]
from .typings import BandArr
import numpy as np


def safe_divide(numerator: np.ndarray, denominator: np.ndarray, default_value=0) -> np.ndarray:
    with np.errstate(divide='ignore', invalid='ignore'):
        result = np.divide(numerator, denominator)
        result[~np.isfinite(result)] = default_value
    return result

def norm_diff_index(band1: BandArr, band2: BandArr, default_value=0) -> BandArr:
    """ Normalized Difference Index:
    - `(band1-band2)/(band1+band2)`
    """
    return safe_divide(band1, band2, default_value=default_value)




def ndvi(nir: BandArr, red: BandArr) -> BandArr:
    """ Normalized Difference Vegetation Index."""
    return norm_diff_index(nir, red)

def ndwi(nir: BandArr, swir: BandArr) -> BandArr:
    """ Normalized Difference Water Index."""
    return norm_diff_index(nir, swir)

def ndbi(swir1: BandArr, nir: BandArr) -> BandArr:
    """ Normalized Difference Built-up Index."""
    return norm_diff_index(swir1, nir)

def ndmi(nir: BandArr, swir1: BandArr) -> BandArr:
    """ Normalized Difference Moisture Index."""
    return norm_diff_index(nir, swir1)

def savi(nir: BandArr, red: BandArr, L=0.5) -> BandArr:
    """ Soil-Adjusted Vegetation Index."""
    assert 0<=L<=1
    return (1 + L) * safe_divide(nir - red, nir + red + L)

def evi(nir: BandArr, red: BandArr, blue: BandArr, L=1, C1=6, C2=7.5, G=2.5) -> BandArr:
    """ Enhanced Vegetation Index."""
    return G * safe_divide(nir - red, nir + C1 * red - C2 * blue + L)

def mndwi(green: BandArr, swir1: BandArr) -> BandArr:
    """ Modified Normalized Difference Water Index."""
    return norm_diff_index(green, swir1)

def bai(nir: BandArr, swir: BandArr) -> BandArr:
    """ Burned Area Index.
    - Nota: `nir` puede ser reemplazado por `red` en ciertas aplicaciónes, investigar.
    """
    return safe_divide(1, (0.1 - nir) ** 2 + (0.06 - swir) ** 2)





def gndvi(nir: BandArr, green: BandArr) -> BandArr:
    """ Green Normalized Difference Vegetation Index (GNDVI) """
    return norm_diff_index(nir, green)

def ndsi(green: BandArr, swir1: BandArr) -> BandArr:
    """ Normalized Difference Snow Index (NDSI) """
    return norm_diff_index(green, swir1)

def msavi(nir: BandArr, red: BandArr) -> BandArr:
    """ Modified Soil Adjusted Vegetation Index (MSAVI) """
    return 0.5 * (2 * (nir + 1) - np.sqrt((2 * nir + 1)**2 - 8 * (nir - red)))

def arvi(nir: BandArr, red: BandArr, blue: BandArr) -> BandArr:
    """ Atmospherically Resistant Vegetation Index (ARVI) """
    return safe_divide(nir - (2 * red - blue), nir + (2 * red - blue))

def gari(nir: BandArr, green: BandArr, red: BandArr, blue: BandArr) -> BandArr:
    """ Green Atmospherically Resistant Index (GARI) """
    return safe_divide(nir - (green - (blue - red)), nir + (green - (blue - red)))

def gvmi(nir: BandArr, swir2: BandArr) -> BandArr:
    """ Global Vegetation Moisture Index (GVMI) """
    return safe_divide((nir + 0.1) - (swir2 + 0.02), (nir + 0.1) + (swir2 + 0.02))

def ndgi(green: BandArr, nir: BandArr) -> BandArr:
    """ Normalized Difference Greenness Index (NDGI) """
    return norm_diff_index(green, nir)

def nbr(nir: BandArr, swir2: BandArr) -> BandArr:
    """ Normalized Burn Ratio (NBR) """
    return norm_diff_index(nir, swir2)

def nbr2(swir1: BandArr, swir2: BandArr) -> BandArr:
    """ Normalized Burn Ratio 2 (NBR2) """
    return norm_diff_index(swir1, swir2)

def ndii(nir: BandArr, swir: BandArr) -> BandArr:
    """ Normalized Difference Infrared Index (NDII) """
    return norm_diff_index(nir, swir)

def ndsii(swir1: BandArr, swir2: BandArr) -> BandArr:
    """ Normalized Difference SII (Soil and Ice Index) (NDSII) """
    return norm_diff_index(swir1, swir2)



# def ndfi(*bands):
#     """ Normalized Difference Fraction Index (NDFI) """
#     # Este índice puede variar en su implementación. A continuación se proporciona una versión genérica.
#     # Se asume que 'bands' es una lista de bandas espectrales en orden específico.
#     return (bands[0] - bands[1]) / (bands[0] + bands[1])


