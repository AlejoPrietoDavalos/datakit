from typing import Generator, List, Tuple

IterPairs = Generator[Tuple[int, int], None, None]

def iter_pairs_chann(n_channels: List[int]) -> IterPairs:
    """ Itera entre 2 pares consecutivos de channels (n-1 iteraciones)."""
    for i in range(len(n_channels) - 1):
        yield n_channels[i], n_channels[i+1]

