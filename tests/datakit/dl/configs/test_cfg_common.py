from datakit.dl.configs import CfgModuleDumpable
from torch import nn

from typing import Type

def assert_module_create(cfg: Type[CfgModuleDumpable]) -> None:
    assert isinstance(cfg.module, nn.Module)
