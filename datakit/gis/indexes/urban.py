from datakit.gis.indexes.common_calcs import norm_diff_index
from numpy import ndarray


def ndbi(swir1: ndarray, nir: ndarray) -> ndarray:
    """ Normalized Difference Built-up Index (NDBI)."""
    return norm_diff_index(swir1, nir)
