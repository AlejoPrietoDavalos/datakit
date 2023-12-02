""" Conjunto de herramientas para aplicar transformaciones sobre imágenes."""
__all__ = ["clip"]

import numpy as np

from rasterio import DatasetReader

from multipledispatch import dispatch


@dispatch(DatasetReader)
def clip(raster: DatasetReader) -> None:
    pass


@dispatch(np.ndarray)
def clip(arr: np.ndarray) -> np.ndarray:
    raise NotImplementedError()
