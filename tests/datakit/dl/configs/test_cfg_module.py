from datakit.dl.configs import CfgModuleDumpable, CfgModule

from torch import nn


class TestCfgModuleDumpable:
    def test_exclude_from_module_dump(self):
        cfg = CfgModuleDumpable()
        _module_dump = cfg.module_dump()
        assert isinstance(cfg.exclude_module_dump, list) and len(cfg.exclude_module_dump) == 0
        assert isinstance(_module_dump, dict)

        for excluid in cfg.exclude_module_dump:
            assert excluid not in _module_dump



class TestCfgModule:
    """ TODO: No hay nada para testear todavia."""
    pass

