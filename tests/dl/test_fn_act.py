from datatools.dl.fn_act import FnAct,FnActNameEnum, FnActModuleEnum

from torch import nn

import pytest


class TestFnActNameEnum:
    def test_name_values_same_str(self) -> None:
        for name, value in FnActNameEnum.iter_name_value_enum():
            assert name==value, "El nombre y el valor deben ser iguales y minúscula."

    def test_default_name(self) -> None:
        pass


class TestFnActModuleEnum:
    def test_moodule_default(self) -> None:
        for module_cls in FnActModuleEnum.iter_value_enum():
            module_default = module_cls()
            assert isinstance(module_default, nn.Module)


@pytest.fixture
def fn_act_default() -> FnAct:
    return FnAct()

class TestFnAct:
    def test_name(self) -> None:
        for name in FnActNameEnum.iter_value_enum():
            fn_act = FnAct(name=name)
            FnActNameEnum.validate_name(name)

    def test_module(self) -> None:
        for name in FnActNameEnum.iter_value_enum():
            fn_act = FnAct(name=name)
            assert isinstance(fn_act.module, nn.Module)

    def test_default(self, fn_act_default: FnAct) -> None:
        assert len(fn_act_default.args) == 0


