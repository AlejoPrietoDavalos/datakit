""" TODO: Ordenar los indices por temática o uso."""
__all__ = ["ndvi"]
from .typings import BandArr


def ndvi(red: BandArr, nir: BandArr) -> BandArr:
    """ Normalized Difference Vegetation Index."""
    return (nir - red) / (nir + red)

def ndwi(nir: BandArr, swir: BandArr) -> BandArr:
    """ Normalized Difference Water Index."""
    return (nir - swir) / (nir + swir)

def ndbi(nir: BandArr, swir: BandArr) -> BandArr:
    """ Normalized Difference Built-up Index."""
    return (swir - nir) / (swir + nir)

def ndmi(nir: BandArr, swir: BandArr) -> BandArr:
    """ Normalized Difference Moisture Index."""
    return (nir - swir) / (nir + swir)

def savi(nir: BandArr, red: BandArr, L=0.5) -> BandArr:
    """ Soil-Adjusted Vegetation Index."""
    assert 0<=L<=1
    return ((nir - red) / (nir + red + L)) * (1 + L)

def evi(nir: BandArr, red: BandArr, blue: BandArr, L=1, C1=6, C2=7.5, G=2.5) -> BandArr:
    """ Enhanced Vegetation Index.
    - TODO: Revisar esos hiperparámetros."""
    return G * ((nir - red) / (nir + C1 * red - C2 * blue + L))

def mndwi(green: BandArr, swir: BandArr) -> BandArr:
    """ Modified Normalized Difference Water Index."""
    return (green - swir) / (green + swir)

def bai(nir: BandArr, swir: BandArr) -> BandArr:
    """ Burned Area Index."""
    #return (1 / ((0.1 - nir) ** 2 + (0.06 - swir) ** 2)) ** 0.5
    raise NotImplementedError("Buscar bien este indice.")
