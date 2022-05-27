import unittest

from ga_app.ga_service.read_file import read_file
from xgraph.algorithms.shortest_paths import dijkstra, bellman_ford, NegativeCycleException
from xgraph.digraph import DiGraph


class TestShortestPaths(unittest.TestCase):
    def setUp(self) -> None:
        edges = [
            ('0', '1', 6),
            ('0', '2', 5),
            ('0', '3', 5),
            ('1', '4', -1),
            ('2', '1', -2),
            ('2', '4', 1),
            ('3', '2', -2),
            ('3', '5', -1),
            ('4', '6', 3),
            ('5', '6', 3),
        ]
        self.bellman_ford_graph_graph = DiGraph(7, edges)
        self.filepath = r'../ga_tests/resources/graph.txt'
        edges, vert_num, _ = read_file(self.filepath)
        self.graph = DiGraph(vert_num, edges)
        self.expected = {
            '0': {'cost': 0, 'path': 'start'},
            '1': {'cost': 4, 'path': '0'},
            '2': {'cost': 12, 'path': '1'},
            '3': {'cost': 8, 'path': '0'},
            '4': {'cost': 14, 'path': '2'},
            '5': {'cost': 16, 'path': '2'},
            '6': {'cost': 9, 'path': '3'},
        }

        neg_cycle_graph, V, _ = read_file(r'../ga_tests/resources/neg_cycle_digraph.txt')
        self.neg_cycle_digraph = DiGraph(vert_num, neg_cycle_graph)

    def test_dijkstra(self):
        sp = dijkstra(self.graph, start='0', representation='adj_list')
        self.assertEqual(self.expected, sp)
        sp = dijkstra(self.graph, start='0', representation='inc_matrix')
        self.assertEqual(self.expected, sp)

    def test_bellman_ford(self):
        sp = bellman_ford(self.bellman_ford_graph_graph, start='0', representation='adj_list')
        expected = {
            '0': {'cost': 0, 'path': 'start'},
            '1': {'cost': 1, 'path': '2'},
            '2': {'cost': 3, 'path': '3'},
            '3': {'cost': 5, 'path': '0'},
            '4': {'cost': 0, 'path': '1'},
            '5': {'cost': 4, 'path': '3'},
            '6': {'cost': 3, 'path': '4'},
        }
        self.assertEqual(expected, sp)

        sp = bellman_ford(self.graph, start='0', representation='adj_list')
        self.assertEqual(self.expected, sp)
        sp = bellman_ford(self.graph, start='0', representation='inc_matrix')
        self.assertEqual(self.expected, sp)

    def test_bellman_ford_detect_negative_cycle(self):
        self.assertRaises(NegativeCycleException, bellman_ford, graph=self.neg_cycle_digraph, start='0', representation='adj_list')
