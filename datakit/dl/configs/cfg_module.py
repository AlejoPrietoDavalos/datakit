from datakit.dl import FnAct

from torch import nn

from pydantic import BaseModel, Field, ConfigDict
from abc import ABC, abstractproperty
from typing import Type, List, Dict, Any

__all__ = ["CfgModuleDumpable", "CfgModule"]

T_Dump = Dict[str, Any]


class _CfgModuleBase(BaseModel, ABC):
    model_config = ConfigDict(validate_assignment=True, frozen=True)


class CfgModuleDumpable(_CfgModuleBase, ABC):
    @property
    def exclude_module_dump(self) -> List[str]:
        """ Elementos a ignorar dentro de `module_dump`."""
        return []

    @property
    def module(self) -> nn.Module:
        """ Instancia el modelo asociado a esta configuración."""
        return self.module_cls(**self.module_dump())
    
    @abstractproperty
    def module_cls(self) -> Type[nn.Module]:
        """ Debe retornar la clase que usará para instanciar."""
        ...
    
    def module_dump(self) -> T_Dump:
        """ Utilizar para instanciar los módulos."""
        return self.model_dump(exclude=self.exclude_module_dump)


class CfgModule(_CfgModuleBase):
    """ Abstract Config Module."""
    fn_act: FnAct = Field(default_factory=FnAct)
