from datakit.dl import FnAct, FnActNameEnum, FnActModuleEnum

from torch import nn

import pytest


class TestFnActNameEnum:
    def test_name_values_same_str(self) -> None:
        for name, value in FnActNameEnum.iter_name_value_enum():
            assert name==value, "El nombre y el valor deben ser iguales y minúscula."

    def test_default_name(self) -> None:
        default_name = FnActNameEnum.default_fn_act_name()
        FnActNameEnum.validate_name(default_name)


class TestFnActModuleEnum:
    def test_default_module(self) -> None:
        for name in FnActNameEnum.iter_name_enum():
            module_cls = FnActModuleEnum.get_module_cls(name)
            module_default = module_cls()
            assert isinstance(module_default, nn.Module)


class TestFnAct:
    def test_default(self) -> None:
        fn_act_default = FnAct()
        assert len(fn_act_default.args) == 0
        FnActNameEnum.validate_name(fn_act_default.name)
    
    def test_name(self) -> None:
        for name in FnActNameEnum.iter_name_enum():
            fn_act = FnAct(name=name)
            FnActNameEnum.validate_name(fn_act.name)

    def test_module(self) -> None:
        for name in FnActNameEnum.iter_value_enum():
            fn_act = FnAct(name=name)
            assert isinstance(fn_act.module, nn.Module)



