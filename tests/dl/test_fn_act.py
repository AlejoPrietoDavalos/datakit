from datatools.dl.fn_act import (
    FnAct,FnActNameEnum, FnActModuleEnum,
    FnActHandler, FN_ACT_NAME)
from datatools.dl.enum_base import iter_name_value_enum, iter_value_enum

from torch import nn

from typing import Type

import pytest


class TestFnActNameEnum:
    @pytest.mark.parametrize(["name", "value"], iter_name_value_enum(FnActNameEnum))
    def test_name_values_same_str(self, name: str, value: str) -> None:
        assert name==value, "El nombre y el valor deben ser iguales y minúscula."

    def test_default_name(self) -> None:
        pass


class TestFnActModuleEnum:
    @pytest.mark.parametrize("module_cls", FnActModuleEnum.iter_module_cls())
    def test_moodule_default(self, module_cls: Type[nn.Module]) -> None:
        module_default = module_cls()
        assert isinstance(module_default, nn.Module)


#class TestFnActHandler:
#    @pytest.mark.parametrize(["name", "module_cls"], FnActHandler.iter_name_module_cls())
#    def test_moodule_default(self, name: str, module_cls: Type[nn.Module]) -> None:
#        module_default = module_cls()
#        assert isinstance(module_default, nn.Module)


class TestFnActEnum:
    pass


@pytest.fixture
def fn_act_default() -> FnAct:
    return FnAct()

class TestFnAct:
    @pytest.mark.parametrize(FN_ACT_NAME, iter_value_enum(FnActNameEnum))
    def test_name(self, name: str) -> None:
        fn_act = FnAct(name=name)
        assert fn_act.name in FnActNameEnum.__members__.values()

    @pytest.mark.parametrize(FN_ACT_NAME, iter_value_enum(FnActNameEnum))
    def test_module(self, name: str) -> None:
        fn_act = FnAct(name=name)
        assert isinstance(fn_act.module, nn.Module)

    def test_default(self, fn_act_default: FnAct) -> None:
        assert len(fn_act_default.args) == 0


