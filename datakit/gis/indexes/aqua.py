from datakit.gis.indexes.common_calcs import norm_diff_index
from numpy import ndarray

def ndwi(nir: ndarray, swir: ndarray) -> ndarray:
    """ Normalized Difference Water Index (NDWI)."""
    return norm_diff_index(nir, swir)

def mndwi(green: ndarray, swir1: ndarray) -> ndarray:
    """ Modified Normalized Difference Water Index (MNDWI)."""
    return norm_diff_index(green, swir1)

def ndmi(nir: ndarray, swir1: ndarray) -> ndarray:
    """ Normalized Difference Moisture Index (NDMI)."""
    return norm_diff_index(nir, swir1)

def ndii(nir: ndarray, swir: ndarray) -> ndarray:
    """ Normalized Difference Infrared Index (NDII) """
    return norm_diff_index(nir, swir)