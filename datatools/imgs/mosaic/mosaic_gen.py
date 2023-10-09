"""
- TODO: Se podría crear una clase que genere y gestione una grilla de una imagen.
- TODO: Se me ocurre una para imagenes generales y otra para rasters.
"""
from __future__ import annotations
#__all__ = ["MosaicGenerator", "MosaicRaster"]

import rasterio
from rasterio import DatasetReader
import numpy as np

from pathlib import Path

from pydantic import BaseModel, ConfigDict


class MosaicRaster(BaseModel):
    asd: int
    @property
    def width(self) -> int:
        return

    def __getitem__(self, idx: int | slice) -> np.ndarray:
        pass


#class MosaicGenerator(BaseModel):
#    """ TODO: Con diferentes modos de generación, tiles de igual tamaño o de tamaño definido."""
#    raster: DatasetReader
    #self.path_folder_out = path_folder_out
    
    #def 