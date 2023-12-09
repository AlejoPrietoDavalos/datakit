'''
from datakit.dl.configs.nn_torch import CfgConv2d, CfgBatchNorm2d
from datakit.dl.configs import CfgConv2dBNAct, CfgMultiConv2dBNAct
from datakit.dl.modules import Conv2dBNAct, MultiConv2dBNAct

import torch

class TestConv2dBNAct:
    def test_forward(self):
        h, w = 32, 32
        for in_channels in range(1, 4):
            out_channels = in_channels*2
            cfg = CfgConv2dBNAct(
                conv2d = CfgConv2d(
                    in_channels = in_channels,
                    out_channels = out_channels,
                    kernel_size = (3, 3),
                    padding = 1
                ),
                bn2d = CfgBatchNorm2d(num_features=out_channels)
            )

            t = torch.rand((1, in_channels, h, w))
            module = Conv2dBNAct(cfg)
            t_out = module(t)
            assert t.shape == t_out.shape
'''