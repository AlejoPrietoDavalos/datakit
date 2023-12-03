from datakit.dl import FnAct

from pydantic import BaseModel, Field, ConfigDict
from abc import ABC
from typing import List, Dict, Any

__all__ = ["CfgModuleDumpable", "CfgModule"]

T_Dump = Dict[str, Any]


class _CfgModuleBase(BaseModel, ABC):
    model_config = ConfigDict(validate_assignment=True, frozen=True)


class CfgModuleDumpable(_CfgModuleBase):
    @property
    def exclude_module_dump(self) -> List[str]:
        """ Elementos a ignorar dentro de `module_dump`."""
        return []
    
    def module_dump(self) -> T_Dump:
        """ Utilizar para instanciar los módulos."""
        return self.model_dump(exclude=self.exclude_module_dump)


class CfgModule(_CfgModuleBase):
    """ Abstract Config Module."""
    fn_act: FnAct = Field(default_factory=FnAct)
