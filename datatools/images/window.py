""" Objetos de datos para utilizar dentro del módulo."""
from __future__ import annotations
__all__ = ["WindowImg"]

from datatools.pydantic_base import BaseModelValAssign

from pydantic import PositiveInt

from rasterio.windows import Window


class WindowImg(BaseModelValAssign):
    """ Rectángulo dentro de una imagen.
    - TODO: Remarcar si agrega o no los bordes."""
    i: PositiveInt
    j: PositiveInt
    height: PositiveInt
    width: PositiveInt

    @property
    def rasterio_window(self) -> Window:
        """ Retorna un `rasterio.windows.Window` para usar con rasterio."""
        return Window(
            col_off = self.i,
            row_off = self.j,
            height = self.height,
            width = self.width
        )


