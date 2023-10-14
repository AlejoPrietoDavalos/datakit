__all__ = ["is_ndarray_2D", "assert_ndarray_2D"]

import numpy as np

def is_ndarray_2D(arr: np.ndarray) -> bool:
    return isinstance(arr, np.ndarray) and len(arr.shape)==2

def assert_ndarray_2D(arr: np.ndarray) -> None:
    if not is_ndarray_2D(arr):
        return ValueError("Debe ser un `np.ndarray` de dimención 2.")
