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
        """ Retorna la clase a usar para instanciar el módulo."""
        ...
    
    @abstractproperty
    def module(self) -> nn.Module:
        """ Instancia el módulo asociado a esta configuración."""
        ...


class CfgModuleDumpable(_CfgModuleBase, ABC):
    @abstractproperty
    def module_cls(self) -> T_Module:
        ...

    @property
    def module(self) -> nn.Module:
        return self.module_cls(**self.module_dump())
    
    @property
    def exclude(self) -> List[str]:
        """ Elementos a ignorar dentro de `module_dump`.
        - FIXME: Todavía no lo usé realmente, vale la pena conservarlo?
        """
        return []

    def module_dump(self) -> T_ModuleDump:
        """ Utilizar para instanciar los módulos."""
        return self.model_dump(exclude=self.exclude)


class CfgModule(_CfgModuleBase):
    """ Abstract Config Module."""
    fn_act: FnAct = Field(default_factory=FnAct)
