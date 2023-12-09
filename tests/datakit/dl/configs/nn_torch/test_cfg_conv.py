""" TODO: Testear los parámetros."""
from datakit.dl.configs.nn_torch import CfgConv2d
from .test_cfg_common import assert_module_create


class TestCfgConv2d:
    def test_module(self):
        cfg = CfgConv2d(
            in_channels = 1,
            out_channels = 10,
            kernel_size = (3, 3)
        )
        assert_module_create(cfg)


