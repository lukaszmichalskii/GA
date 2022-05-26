import random
import unittest

from ga_tests.utils import is_heap
from xgraph.data_structures.heap import HeapAdjVertices


class TestHeap(unittest.TestCase):
    def setUp(self) -> None:
        self.heap_adj_vertices = HeapAdjVertices()
        self.size = 10
        for i in range(self.size):
            self.heap_adj_vertices.add((str(i), random.randrange(0, 10)))

    def test_add(self):
        self.assertTrue(is_heap(self.heap_adj_vertices.array))

    def test_add_all(self):
        iterable = [(str(i), random.randint(0, 10)) for i in range(6)]
        self.heap_adj_vertices.add_all(iterable)
        self.assertTrue(is_heap(self.heap_adj_vertices.array))

    def test_remove(self):
        while self.heap_adj_vertices.size > 0:
            self.heap_adj_vertices.remove()
            self.assertTrue(is_heap(self.heap_adj_vertices.array))

