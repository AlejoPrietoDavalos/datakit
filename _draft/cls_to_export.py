from typing import Type, List

def cls2export(list_cls: List[Type]) -> List[Type]:
    """
    - Recibe una lista de clases a exportar dentro de __all__.
    
    Usage:
    ------
        ```python
        # Dentro de `my_module.py`.
        __all__ = cls2export([PublicClass_1, PublicClass_2])
        class PublicClass_1: ...
        class PublicClass_2: ...
        class PrivateClass: ...

        # Dentro de `__init__.py`
        from .my_module import *
        ```
    """
    return [cls.__name__ for cls in list_cls]
