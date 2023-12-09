from datakit.dl.configs import CfgModuleDump
from torch import nn

from typing import Type

def assert_module_create(cfg: Type[CfgModuleDump]) -> None:
    assert isinstance(cfg.module, nn.Module)
