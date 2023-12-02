import pytest

from datatools.dl.configs import CfgModuleBase, CfgModule
from datatools.dl.fn_act import FnActEnum, FnActHandler

from torch import nn

from typing import Type

@pytest.fixture
def cfg_module_base():
    return CfgModuleBase()


def _test_cfgs_module_dump(cfg: Type[CfgModuleBase]) -> None:
    cfg_module_dump = cfg.module_dump()
    assert isinstance(cfg_module_dump, dict)
    

def _test_cfgs_exclude_not_in_module_dump(cfg: Type[CfgModuleBase]) -> None:
    assert isinstance(cfg.exclude, list)
    _module_dump = cfg.module_dump()
    for excluid in cfg.exclude:
        assert excluid not in _module_dump

def _test_exclude_from_module_dump(cfg: Type[CfgModuleBase]):
    _test_cfgs_exclude_not_in_module_dump(cfg)
    _test_cfgs_module_dump(cfg)


class TestCfgModuleBase:
    def test_exclude_from_module_dump(self, cfg_module_base: CfgModuleBase):
        _test_exclude_from_module_dump(cfg_module_base)

class TestCfgModule:
    def test_exclude_from_module_dump(self):
        for fn_enum in FnActEnum:
            fn_act_name = fn_enum.value
            cfg = CfgModule(fn_act_name=fn_act_name)
            
            _test_exclude_from_module_dump(cfg)
            assert cfg.fn_act_name == fn_act_name
            assert isinstance(cfg.fn_act_args, dict)
            assert len(cfg.fn_act_args)==0  # Por defecto no debería tener argumentos.
            assert isinstance(cfg.fn_act, nn.Module)

