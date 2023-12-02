from datatools.dl.fn_act import FnActHandler, FnActEnum, exclude_fn_act
from pydantic import BaseModel, Field, ConfigDict
from abc import ABC

__all__ = ["CfgModuleBase", "CfgModule"]


class CfgModuleBase(BaseModel, ABC):
    model_config = ConfigDict(validate_assignment=True, use_enum_values=True)
    @property
    def exclude(self) -> list:
        """ Elementos a ignorar dentro de `module_dump`."""
        return []
    
    def module_dump(self) -> dict:
        return self.model_dump(exclude=self.exclude)


class CfgModule(CfgModuleBase, ABC):
    """ Abstract Config Module."""
    fn_act_name: FnActEnum = Field(default=FnActEnum.RELU.value)
    fn_act_args: dict = Field(default_factory=dict)
    
    @property
    def fn_act(self):
        return FnActHandler.get_fn_act(self.fn_act_name, self.fn_act_args)

    @property
    def exclude(self) -> list:
        return exclude_fn_act()
