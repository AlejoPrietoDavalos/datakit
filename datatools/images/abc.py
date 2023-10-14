__all__ = ["AbstractImg"]
from datatools.pydantic_base import BaseModelValAssign

from abc import ABC, abstractproperty

class AbstractImg(BaseModelValAssign, ABC):
    @abstractproperty
    def height(self) -> int: ...
    @abstractproperty
    def width(self) -> int: ...
