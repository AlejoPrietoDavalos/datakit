""" Versión usando `Pydantic` de `torch.nn.common_types` de `PyTorch`."""
from torch.nn.common_types import (
    _scalar_or_tuple_any_t,
    _scalar_or_tuple_2_t
)
from torch import nn
from pydantic import NonNegativeInt
from typing import TypeVar, Type, Dict, Any

__all__ = ["T_Module", "_size_any_t",
           "_size_1_t", "_size_2_t", "_size_3_t",
           "_size_4_t", "_size_5_t", "_size_6_t"]


T_Module = TypeVar('T_Module', bound=Type[nn.Module])
T_ModuleDump = Dict[str, Any]

# For arguments which represent size parameters (eg, kernel size, padding)
_size_any_t = _scalar_or_tuple_any_t[NonNegativeInt]
#_size_1_t = _scalar_or_tuple_1_t[NonNegativeInt]
_size_2_t = _scalar_or_tuple_2_t[NonNegativeInt]
#_size_3_t = _scalar_or_tuple_3_t[NonNegativeInt]
#_size_4_t = _scalar_or_tuple_4_t[NonNegativeInt]
#_size_5_t = _scalar_or_tuple_5_t[NonNegativeInt]
#_size_6_t = _scalar_or_tuple_6_t[NonNegativeInt]

# For arguments which represent optional size parameters (eg, adaptive pool parameters)
#_size_any_opt_t = _scalar_or_tuple_any_t[Optional[NonNegativeInt]]
#_size_2_opt_t = _scalar_or_tuple_2_t[Optional[NonNegativeInt]]
#_size_3_opt_t = _scalar_or_tuple_3_t[Optional[NonNegativeInt]]

# For arguments that represent a ratio to adjust each dimension of an input with (eg, upsampling parameters)
#_ratio_2_t = _scalar_or_tuple_2_t[float]
#_ratio_3_t = _scalar_or_tuple_3_t[float]
#_ratio_any_t = _scalar_or_tuple_any_t[float]

#_tensor_list_t = _scalar_or_tuple_any_t[Tensor]

# For the return value of max pooling operations that may or may not return indices.
# With the proposed 'Literal' feature to Python typing, it might be possible to
# eventually eliminate this.
#_maybe_indices_t = _scalar_or_tuple_2_t[Tensor]

