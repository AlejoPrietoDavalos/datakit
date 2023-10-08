"""
- TODO: Se podría crear una clase que genere y gestione una grilla de una imagen.
- TODO: Se me ocurre una para imagenes generales y otra para rasters.
"""
from rasterio import DatasetReader
import numpy as np

from pydantic import BaseModel, ConfigDict

class MosaicRaster(BaseModel):
    raster: DatasetReader
    
    @property
    def width(self) -> int:
        return

    def __getitem__(self, idx: int | slice) -> np.ndarray:
        pass


class MosaicGenerator:
    pass