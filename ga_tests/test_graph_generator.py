import unittest

from ga_app.ga_service.graph_generator import GraphGenerator
from ga_tests.utils import depth_first_search
from xgraph.digraph import DiGraph
from xgraph.graph import Graph


class TestGraphGenerator(unittest.TestCase):
    def setUp(self) -> None:
        self.GG = GraphGenerator()
        self.V = 10

    def test_vertices_num(self):
        DiG: DiGraph = self.GG.generate_graph(self.V, True)
        G: Graph = self.GG.generate_graph(self.V, False)
        self.assertTrue(DiG.is_directed)
        self.assertFalse(G.is_directed)
        self.assertEqual(len(DiG.vertices), self.V)
        self.assertEqual(len(G.vertices), self.V)

    def test_graph_connectivity(self):
        G: Graph = self.GG.generate_graph(self.V, False)
        self.assertEqual(len(G.vertices), len(depth_first_search(G, '0')))
