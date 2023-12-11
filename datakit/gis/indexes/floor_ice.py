from datakit.gis.indexes.common_calcs import norm_diff_index
from numpy import ndarray

__all__ = ["ndsi", "ndsii"]

def ndsi(green: ndarray, swir1: ndarray) -> ndarray:
    """ Normalized Difference Snow Index (NDSI)."""
    return norm_diff_index(green, swir1)

def ndsii(swir1: ndarray, swir2: ndarray) -> ndarray:
    """ Normalized Difference SII (Soil and Ice Index) (NDSII)."""
    return norm_diff_index(swir1, swir2)