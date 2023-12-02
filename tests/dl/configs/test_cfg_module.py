import pytest

from datakit.dl.configs import CfgModuleBase, CfgModule
from datakit.dl.fn_act import FnActNameEnum, FN_ACT_NAME

from torch import nn

from typing import Type



########### Para probar subclases de CfgModuleBase - Mejorar ###########
def _test_cfgs_module_dump(cfg: Type[CfgModuleBase]) -> None:
    cfg_module_dump = cfg.module_dump()
    assert isinstance(cfg_module_dump, dict)

def _test_cfgs_exclude_not_in_module_dump(cfg: Type[CfgModuleBase]) -> None:
    assert isinstance(cfg.exclude_module_dump, list)
    _module_dump = cfg.module_dump()
    for excluid in cfg.exclude_module_dump:
        assert excluid not in _module_dump

def _test_exclude_from_module_dump(cfg: Type[CfgModuleBase]):
    _test_cfgs_exclude_not_in_module_dump(cfg)
    _test_cfgs_module_dump(cfg)
########### Para probar subclases de CfgModuleBase - Mejorar ###########





@pytest.fixture
def cfg_module_base():
    return CfgModuleBase()

class TestCfgModuleBase:
    def test_exclude_from_module_dump(self, cfg_module_base: CfgModuleBase):
        _test_exclude_from_module_dump(cfg_module_base)



#class TestCfgModule:
#    @pytest.mark.parametrize(FN_ACT_NAME, [fn_enum.value for fn_enum in FnActEnum])
#    def test_exclude_from_module_dump(self, fn_act_name):
#        cfg = CfgModule(fn_act_name=fn_act_name)
#        
#        _test_exclude_from_module_dump(cfg)
#        assert cfg.fn_act.name == fn_act_name
#        assert isinstance(cfg.fn_act.args, dict) and len(cfg.fn_act_args)==0
#        assert isinstance(cfg.fn_act.module, nn.Module)

