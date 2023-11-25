from torch import nn

from enum import Enum
from typing import Type

__all__ = ["FnActEnum", "FnActHandler"]


class FnActEnum(str, Enum):
    RELU = "relu"
    PRELU = "prelu"
    LEAKY_RELU = "leaky_relu"
    SIGMOID = "sigmoid"
    SOFTMAX = "softmax"
    TANH = "tanh"
    ELU = "elu"
    MISH = "mish"


class FnActHandler:
    """ Mapea el nombre de la función de activación con su análogo en Pytorch."""
    _handler = {
        FnActEnum.RELU: nn.ReLU,
        FnActEnum.PRELU: nn.PReLU,
        FnActEnum.LEAKY_RELU: nn.LeakyReLU,
        FnActEnum.SIGMOID: nn.Sigmoid,
        FnActEnum.SOFTMAX: nn.Softmax,
        FnActEnum.TANH: nn.Tanh,
        FnActEnum.ELU: nn.ELU,
        FnActEnum.MISH: nn.Mish,
    }

    @classmethod
    def get_fn_act(cls, fn_act_name: str, fn_act_args: dict) -> Type[nn.Module]:
        """ Retorna la función de activación según su nombre."""
        if fn_act_name not in cls._handler:
            raise ValueError("Función de activación inválida.")
        return cls._handler[fn_act_name](**fn_act_args)
