from datatools.dl.enum_base import iter_value_enum

from torch import nn

from pydantic import BaseModel, Field, ConfigDict

from functools import cached_property
from enum import Enum, StrEnum, auto
from typing import Type, Generator, Tuple, TypeVar, Any

__all__ = ["FnAct", "FnActNameEnum", "FnActModuleEnum", "FnActHandler"]

FN_ACT_NAME = "name"
FN_ACT_ARGS = "args"



class FnActNameEnum(StrEnum):
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


class FnActModuleEnum(Enum):
    """ Mapea el nombre de la función de activación con su análogo en Pytorch."""
    relu = nn.ReLU
    prelu = nn.PReLU
    leaky_relu = nn.LeakyReLU
    sigmoid = nn.Sigmoid
    softmax = nn.Softmax
    tanh = nn.Tanh
    elu = nn.ELU
    mish = nn.Mish

    @classmethod
    def iter_module_cls(cls) -> Type[nn.Module]:
        return (module_cls for module_cls in iter_value_enum(cls))

    @classmethod
    def get_module_cls(cls, name: str) -> Type[nn.Module]:
        return cls[name].value


class FnActHandler:
    """ Mapea el nombre de la función de activación con su módulo."""
    @classmethod
    def iter_name_module_cls(cls) -> Generator[Tuple[str, Type[nn.Module]], None, None]:
        for name in FnActNameEnum.__members__.keys():
            module_cls = cls.get_fn_act_module(name)
            yield name, module_cls
    
    @classmethod
    def get_fn_act_module(cls, name: str) -> Type[nn.Module]:
        """ Retorna la función de activación según su nombre."""
        # Comprobar que sea un nombre valido en el Enum.
        FnActNameEnum.validate_name(name)

        cls_fn_module = FnActModuleEnum.get_module_cls(name)
        return cls_fn_module


class FnAct(BaseModel):
    model_config = ConfigDict(validate_assignment=True, use_enum_values=True)
    name: FnActNameEnum = Field(default=FnActNameEnum.default_fn_act_name())
    args: dict = Field(default_factory=dict)

    @cached_property
    def module(self) -> nn.Module:
        """ Retorna el módulo asociado a la función de activación `name`."""
        cls_fn_module = FnActHandler.get_fn_act_module(self.name)
        fn_module = cls_fn_module(**self.args)
        return fn_module
