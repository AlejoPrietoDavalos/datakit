from datakit.dl.configs import CfgBatchNorm2d

from .test_cfg_common import assert_module_create

class TestCfgBatchNorm2d:
    def test_module(self) -> None:
        cfg = CfgBatchNorm2d(num_features=128)
        assert_module_create(cfg)