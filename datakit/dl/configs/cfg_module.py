from datakit.dl import FnAct

from torch import nn

from pydantic import BaseModel, Field, ConfigDict
from abc import ABC, abstractproperty
from datakit.dl.common_types import T_Module, T_ModuleDump
from typing import List

__all__ = ["CfgModuleDumpable", "CfgModule"]


class _CfgModuleBase(BaseModel, ABC):
    model_config = ConfigDict(validate_assignment=True, use_enum_values=True, frozen=True)

    @abstractproperty
    def module_cls(self) -> T_Module:
        """ Debe retornar la clase que usará para instanciar."""
        ...
    
    @abstractproperty
    def module(self) -> nn.Module:
        """ Instancia el módulo asociado a esta configuración."""
        ...


class CfgModuleDumpable(_CfgModuleBase, ABC):
    @property
    def exclude_module_dump(self) -> List[str]:
        """ Elementos a ignorar dentro de `module_dump`."""
        return []

    @property
    def module(self) -> nn.Module:
        return self.module_cls(**self.module_dump())

    def module_dump(self) -> T_ModuleDump:
        """ Utilizar para instanciar los módulos."""
        return self.model_dump(exclude=self.exclude_module_dump)


class CfgModule(_CfgModuleBase):
    """ Abstract Config Module."""
    fn_act: FnAct = Field(default_factory=FnAct)
