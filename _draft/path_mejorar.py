from pathlib import Path

from functools import cached_property

import attr
from attr.validators import instance_of

@attr.s(frozen=True)
class FileStructDS:
    root: Path = attr.ib(validator=instance_of(Path))

    @cached_property
    def data(self) -> Path: return self.root / "data"
    @cached_property
    def raw(self) -> Path: return self.data / "raw"
    @cached_property
    def preprocess(self) -> Path: return self.data / "preprocess"
    @cached_property
    def processed(self) -> Path: return self.data / "processed"
