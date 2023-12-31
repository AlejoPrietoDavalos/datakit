from datakit.enum_base import EnumIter, StrEnumIter

from torch import nn

from pydantic import BaseModel, Field, ConfigDict

from enum import auto
from datakit.dl.common_types import T_Module
from typing import Type

__all__ = ["FnActNameEnum", "FnActModuleEnum", "FnAct"]


class FnActNameEnum(StrEnumIter):
    relu = auto()
    prelu = auto()
    leaky_relu = auto()
    sigmoid = auto()
    softmax = auto()
    tanh = auto()
    elu = auto()
    mish = auto()

    @classmethod
    def default_fn_act_name(cls) -> str:
        return cls.relu.name

    @classmethod
    def validate_name(cls, name: str) -> None:
        if name not in FnActNameEnum.__members__.keys():
            raise ValueError("Función de activación inválida.")


class FnActModuleEnum(EnumIter):
    """ Mapea el nombre de la función de activación con su módulo."""
    relu = nn.ReLU
    prelu = nn.PReLU
    leaky_relu = nn.LeakyReLU
    sigmoid = nn.Sigmoid
    softmax = nn.Softmax
    tanh = nn.Tanh
    elu = nn.ELU
    mish = nn.Mish

    @classmethod
    def get_module_cls(cls, name: str) -> T_Module:
        """ Retorna la función de activación según su nombre."""
        FnActNameEnum.validate_name(name)
        return cls.name2value(name)


class FnAct(BaseModel):
    model_config = ConfigDict(validate_assignment=True, use_enum_values=True, frozen=True)
    name: FnActNameEnum = Field(default=FnActNameEnum.default_fn_act_name())
    args: dict = Field(default_factory=dict)

    @property
    def module(self) -> nn.Module:
        """ Retorna el módulo asociado a la función de activación `name`."""
        module_cls = FnActModuleEnum.get_module_cls(self.name)
        module = module_cls(**self.args)
        return module
