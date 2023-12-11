from datakit.gis.indexes.common_calcs import safe_divide, norm_diff_index
from numpy import ndarray

__all__ = ["bai", "nbr", "nbr2"]

def bai(nir: ndarray, swir: ndarray) -> ndarray:
    """ Burned Area Index (BAI).
    - Nota: `nir` puede ser reemplazado por `red` en ciertas aplicaciónes, investigar.
    """
    return safe_divide(1, (0.1 - nir) ** 2 + (0.06 - swir) ** 2)

def nbr(nir: ndarray, swir2: ndarray) -> ndarray:
    """ Normalized Burn Ratio (NBR)."""
    return norm_diff_index(nir, swir2)

def nbr2(swir1: ndarray, swir2: ndarray) -> ndarray:
    """ Normalized Burn Ratio 2 (NBR2)."""
    return norm_diff_index(swir1, swir2)


