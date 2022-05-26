import unittest

from ga_app.ga_service.read_file import read_file
from xgraph.digraph import DiGraph


class TestDiGraph(unittest.TestCase):
    def setUp(self) -> None:
        filepath = r'../ga_tests/resources/graph.txt'
        self.edges, vert_num, _ = read_file(filepath)
        self.digraph = DiGraph(vert_num, self.edges)

    def test_adj_list(self):
        expected = {
            '0': [('1', 4), ('3', 8)],
            '1': [('2', 8), ('3', 11)],
            '2': [('4', 2), ('5', 4)],
            '3': [('4', 7), ('6', 1)],
            '4': [('6', 6)],
            '5': [('6', 2)],
            '6': [],
        }
        self.assertTrue(expected, self.digraph.adj_list)

    def test_inc_matrix(self):
        expected = [[4, 8, 0, 0, 0, 0, 0, 0, 0, 0],
                    [-4, 0, 8, 11, 0, 0, 0, 0, 0, 0],
                    [0, 0, -8, 0, 2, 4, 0, 0, 0, 0],
                    [0, -8, 0, -11, 0, 0, 7, 1, 0, 0],
                    [0, 0, 0, 0, -2, 0, -7, 0, 6, 0],
                    [0, 0, 0, 0, 0, -4, 0, 0, 0, 2],
                    [0, 0, 0, 0, 0, 0, 0, -1, -6, -2]]
        self.assertTrue(expected, self.digraph.inc_matrix)
