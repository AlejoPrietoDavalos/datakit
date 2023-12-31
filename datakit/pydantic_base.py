""" Clases base de pydantic para usar dentro del módulo."""
__all__ = ["BaseModelValAssign"]

from pydantic import BaseModel, ConfigDict

class BaseModelValAssign(BaseModel):
    """ BaseModel que valida la asignación de properties."""
    model_config = ConfigDict(validate_assignment=True)
