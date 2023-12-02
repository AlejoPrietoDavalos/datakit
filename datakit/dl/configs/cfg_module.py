from datatools.dl.fn_act import FnAct

from pydantic import BaseModel, Field, ConfigDict
from abc import ABC, abstractproperty

from datatools.dl.common_types import T_Dump
from typing import List

__all__ = ["CfgModuleBase", "CfgModule"]


class _CfgModuleBase(BaseModel, ABC):
    model_config = ConfigDict(validate_assignment=True, frozen=True)

    @abstractproperty
    def exclude_module_dump(self) -> List[str]:
        """ Elementos a ignorar dentro de `module_dump`."""
        ...

    def module_dump(self) -> T_Dump:
        """ Utilizar para instanciar los módulos."""
        return self.model_dump(exclude=self.exclude_module_dump)


class CfgModuleBase(_CfgModuleBase, ABC):
    @property
    def exclude_module_dump(self) -> List[str]:
        return []


class CfgModule(CfgModuleBase, ABC):
    """ Abstract Config Module."""
    fn_act: FnAct = Field(default_factory=FnAct)

    @property
    def exclude_module_dump(self) -> List[str]:
        return ["fn_act"]
