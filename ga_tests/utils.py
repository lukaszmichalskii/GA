from typing import List, Tuple, Union, Set

from xgraph.digraph import DiGraph
from xgraph.graph import Graph


def is_heap(array: List[Tuple[str, int]]):
    if len(array) <= 1:
        return True
    for i in range((len(array) - 2) // 2 + 1):
        if array[i][1] > array[2 * i + 1][1] or (2 * i + 2 != len(array) and array[i][1] > array[2 * i + 2][1]):
            return False
    return True
