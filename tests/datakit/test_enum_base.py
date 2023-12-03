from datakit.enum_base import EnumIter, StrEnumIter

def iter_enums_to_test():
    yield EnumIter
    yield StrEnumIter

def test_empty_enum():
    for enum_cls in iter_enums_to_test():
        assert len(list(enum_cls.iter_name_enum())) == 0
        assert len(list(enum_cls.iter_value_enum())) == 0
        assert len(list(enum_cls.iter_name_value_enum())) == 0
