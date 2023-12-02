
from enum import Enum, StrEnum
from typing import TypeVar, Tuple, Type, Generator, Any

T = TypeVar("T")
K = TypeVar("K")
_tuple_2_t = Tuple[T, K]

_name_enum, _value_enum = str, Any
_name_value_enum = _tuple_2_t[_name_enum, _value_enum]

gen_name_value_enum = Generator[_name_value_enum, None, None]
gen_name_enum = Generator[_name_enum, None, None]
gen_value_enum = Generator[_value_enum, None, None]



# Esto se podría hacer con herencia.
def iter_name_value_enum(enum: Type[Enum]) -> gen_name_value_enum:
    return ((name, enum.value) for name, enum in enum.__members__.items())


class BaseEnumIterMethods:
    @classmethod
    def iter_name_value_enum(cls) -> Generator[_tuple_2_t, None, None]:
        return ((name, value) for name, value in iter_name_value_enum(cls))

    @classmethod
    def iter_name_enum(cls) -> Generator[str, None, None]:
        return (name for name, _ in cls.iter_name_value_enum())

    @classmethod
    def iter_value_enum(cls) -> Generator[Any, None, None]:
        return (value for _, value in cls.iter_name_value_enum())


class EnumIter(BaseEnumIterMethods, Enum):
    pass


class StrEnumIter(BaseEnumIterMethods, StrEnum):
    pass


'''
class EnumIter(Enum):
    @classmethod
    def iter_name_value_enum(cls) -> Generator[_tuple_2_t, None, None]:
        return ((name, enum.value) for name, enum in cls.__members__.items())

    @classmethod
    def iter_name_enum(cls: Type[Enum]) -> Generator[str, None, None]:
        return (name for name, _ in iter_name_enum(cls))

    @classmethod
    def iter_value_enum(cls: Type[Enum]) -> Generator[Any, None, None]:
        return (value for _, value in iter_value_enum(cls))

class StrEnumIter(StrEnum):
    @classmethod
    def iter_name_value_enum(cls) -> Generator[_tuple_2_t, None, None]:
        return ((name, enum.value) for name, enum in cls.__members__.items())

    @classmethod
    def iter_name_enum(cls: Type[Enum]) -> Generator[str, None, None]:
        return (name for name, _ in iter_name_enum(cls))

    @classmethod
    def iter_value_enum(cls: Type[Enum]) -> Generator[Any, None, None]:
        return (value for _, value in iter_value_enum(cls))

'''