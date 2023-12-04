from datakit.dl.configs import CfgModuleDumpable, CfgConv2d

from torch import nn

from typing import Type

def assert_module_create(cfg: Type[CfgModuleDumpable]) -> None:
    assert isinstance(cfg.module, nn.Module)

class TestCfgConv2d:
    def test_module(self):
        cfg = CfgConv2d(
            in_channels = 1,
            out_channels = 10,
            kernel_size = (3,3)
        )
        assert_module_create(cfg)


