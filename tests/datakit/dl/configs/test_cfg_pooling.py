from datakit.dl.configs import CfgMaxPool2d
from .test_cfg_common import assert_module_create

class TestCfgMaxPool2d:
    def test_module(self):
        cfg = CfgMaxPool2d(kernel_size=(3, 3))
        assert_module_create(cfg)

