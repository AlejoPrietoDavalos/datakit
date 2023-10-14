"""
- TODO: Se podría crear una clase que genere y gestione una grilla de una imagen.
- TODO: Se me ocurre una para imagenes generales y otra para rasters.
"""
from __future__ import annotations
__all__ = ["MosaicConfig", "mosaic2tiles"]

import rasterio
from rasterio.windows import Window
from rasterio import DatasetReader
import numpy as np

from pathlib import Path
import os

from pydantic import BaseModel, ConfigDict, Field
from typing import NewType


class MosaicConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    
    path_raster_in: Path = Field(frozen=True)
    output_folder: Path = Field(frozen=True)
    tile_width: int
    tile_height: int





def mosaic2tiles(conf: MosaicConfig):
    conf.output_folder.mkdir(exist_ok=True)

    with rasterio.open(conf.path_raster_in) as raster_mosaic:
        meta = raster_mosaic.meta.copy()
        total_width = raster_mosaic.meta['width']
        total_height = raster_mosaic.meta['height']

        for i, h in enumerate(range(0, total_height, conf.tile_height)):
            for j, w in enumerate(range(0, total_width, conf.tile_width)):
                # Esta parte recorta.
                window = Window(
                    col_off = w,
                    row_off = h,
                    width = conf.tile_width,
                    height = conf.tile_height
                )
                transform = rasterio.windows.transform(window, raster_mosaic.transform)

                meta['transform'] = transform
                meta['width'], meta['height'] = window.width, window.height

                output_path = conf.output_folder / f"tile_{i}_{j}.tif"
                
                with rasterio.open(output_path, 'w', **meta) as dst:
                    dst.write(raster_mosaic.read(window=window))
                # Esta parte recorta.



#Width = NewType("width", int)
#Height = NewType("height", int)
#Pos_ij = NewType("pos_ij", tuple[int, int])

'''
class MosaicGenerator:
    """
    Dentro se ordenan 

    TODO: Con diferentes modos de generación, tiles de igual tamaño o de tamaño definido."""
    def __init__(self, path_raster_mosaic: Path, path_folder_out: Path):
        self.path_raster_mosaic = path_raster_mosaic
        self.path_folder_out = path_folder_out

        # Abrir para extraer la metadata, guardarla y cerrarlo.

    #@property
    #def width(self) -> Width:
    #    return self.raster.width
    
    #@property
    #def height(self) -> Height:
    #    return self.raster.height
    
    def tile_width(self, idx: int | Pos_ij) -> Width:
        return self.raster
    
    def tile_height(self, idx: int | Pos_ij) -> Height:
        return self.raster
    
    def create(self) -> None:
        pass
'''
