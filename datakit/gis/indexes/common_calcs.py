import numpy as np
from numpy import ndarray

__all__ = ["safe_divide", "norm_diff_index"]

def safe_divide(numerator: ndarray, denominator: ndarray, default_value=0) -> ndarray:
    """ División de arrays controlando la división por 0.
    - `default_value:` Valor por default cuando se divide por 0."""
    with np.errstate(divide='ignore', invalid='ignore'):
        result = np.divide(numerator, denominator)
        result[~np.isfinite(result)] = default_value
    return result

def norm_diff_index(band1: ndarray, band2: ndarray, default_value=0) -> ndarray:
    """ Normalized Difference Index:
    - `(band1-band2)/(band1+band2)`
    """
    return safe_divide(band1, band2, default_value=default_value)
