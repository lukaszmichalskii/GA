import math
from typing import List, Tuple

from xgraph.data_structures.edge import Edge


class HeapAdjVertices:
    def __init__(self):
        self._heap: List[Tuple[str, int]] = list()

    def add(self, item: Tuple[str, int]) -> None:
        self._heap.append(item)
        last_position: int = len(self._heap)-1
        self._trickle_up(last_position)

    def add_all(self, iterable: List[Tuple[str, int]]) -> None:
        for item in iterable:
            self.add(item)

    def remove(self) -> Tuple[str, int]:
        if self.size <= 0:
            raise EmptyHeapException
        self._swap(0, len(self._heap)-1)
        root = self._heap.pop(-1)
        self._trickle_down(0)
        return root

    def _trickle_up(self, position: int) -> None:
        if position == 0:
            return
        parent: int = int(math.floor((position-1)/2))
        if self._heap[position][1] < self._heap[parent][1]:
            self._swap(position, parent)
            self._trickle_up(parent)

    def _trickle_down(self, parent: int) -> None:
        left: int = 2*parent+1
        right: int = 2*parent+2
        last_position = len(self._heap)-1
        if left == last_position and self._heap[left][1] < self._heap[parent][1]:
            self._swap(parent, left)
            return
        if right == last_position and self._heap[right][1] < self._heap[parent][1]:
            if self._heap[right][1] < self._heap[left][1]:
                self._swap(parent, right)
                return
            self._swap(parent, left)
            return
        if left > last_position or right > last_position:
            return
        if self._heap[left][1] < self._heap[right][1] and self._heap[left][1] < self._heap[parent][1]:
            self._swap(parent, left)
            self._trickle_down(left)
        elif self._heap[right][1] < self._heap[parent][1]:
            self._swap(parent, right)
            self._trickle_down(right)

    def _swap(self, from_index: int, to_index: int) -> None:
        self._heap[from_index], self._heap[to_index] = self._heap[to_index], self._heap[from_index]

    @property
    def array(self):
        return self._heap

    @property
    def size(self):
        return len(self._heap)

    def __str__(self):
        return str(self._heap)


class HeapEdges:
    def __init__(self):
        self._heap: List[Edge] = list()

    def add(self, item: Edge) -> None:
        self._heap.append(item)
        last_position: int = len(self._heap)-1
        self._trickle_up(last_position)

    def add_all(self, iterable: List[Edge]) -> None:
        for item in iterable:
            self.add(item)

    def remove(self) -> Edge:
        if self.size <= 0:
            raise EmptyHeapException
        self._swap(0, len(self._heap)-1)
        root = self._heap.pop(-1)
        self._trickle_down(0)
        return root

    def _trickle_up(self, position: int) -> None:
        if position == 0:
            return
        parent: int = int(math.floor((position-1)/2))
        if self._heap[position].weight < self._heap[parent].weight:
            self._swap(position, parent)
            self._trickle_up(parent)

    def _trickle_down(self, parent: int) -> None:
        left: int = 2*parent+1
        right: int = 2*parent+2
        last_position = len(self._heap)-1
        if left == last_position and self._heap[left].weight < self._heap[parent].weight:
            self._swap(parent, left)
            return
        if right == last_position and self._heap[right].weight < self._heap[parent].weight:
            if self._heap[right].weight < self._heap[left].weight:
                self._swap(parent, right)
                return
            self._swap(parent, left)
            return
        if left > last_position or right > last_position:
            return
        if self._heap[left].weight < self._heap[right].weight and self._heap[left].weight < self._heap[parent].weight:
            self._swap(parent, left)
            self._trickle_down(left)
        elif self._heap[right].weight < self._heap[parent].weight:
            self._swap(parent, right)
            self._trickle_down(right)

    def _swap(self, from_index: int, to_index: int) -> None:
        self._heap[from_index], self._heap[to_index] = self._heap[to_index], self._heap[from_index]

    @property
    def array(self):
        return self._heap

    @property
    def size(self):
        return len(self._heap)

    def __str__(self):
        return str(self._heap)


class EmptyHeapException(Exception):
    pass
