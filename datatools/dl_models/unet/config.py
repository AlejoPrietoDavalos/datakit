from pydantic import BaseModel, Field

from typing import List

class UNETConfig(BaseModel):
    n_bands_in: int
    n_bands_out: int
    channels: List[int]

    @property
    def botton_channel(self) -> int:
        return self.channels[-1]

    @property
    def encoder_channels(self) -> List[int]:
        return [self.n_bands_in] + self.channels[:-1]
    
    @property
    def decoder_channels(self) -> List[int]:
        asd = self.channels.copy()
        asd.reverse()
        return asd