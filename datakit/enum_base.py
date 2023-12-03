from enum import Enum, StrEnum
from typing import TypeVar, Tuple, Type, Generator, Any

__all__ = ["EnumIter", "StrEnumIter"]


T = TypeVar("T")
K = TypeVar("K")
_tuple_2_t = Tuple[T, K]

_name_enum, _value_enum = str, Any
_name_value_enum = _tuple_2_t[_name_enum, _value_enum]

gen_name_value_enum = Generator[_name_value_enum, None, None]
gen_name_enum = Generator[_name_enum, None, None]
gen_value_enum = Generator[_value_enum, None, None]



def iter_name_value_enum(enum: Type[Enum]) -> gen_name_value_enum:
    return ((name, enum.value) for name, enum in enum.__members__.items())


class _BaseEnumIterMethods:
    @classmethod
    def iter_name_value_enum(cls) -> gen_name_value_enum:
        return ((name, value) for name, value in iter_name_value_enum(cls))

    @classmethod
    def iter_name_enum(cls) -> gen_name_enum:
        return (name for name, _ in cls.iter_name_value_enum())

    @classmethod
    def iter_value_enum(cls) -> gen_value_enum:
        return (value for _, value in cls.iter_name_value_enum())

    @classmethod
    def name2value(cls: Type[Enum], name: str) -> _value_enum:
        return cls[name].value

class EnumIter(_BaseEnumIterMethods, Enum):
    pass


class StrEnumIter(_BaseEnumIterMethods, StrEnum):
    pass
