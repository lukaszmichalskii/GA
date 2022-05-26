import unittest

from ga_app.ga_service.read_file import read_file
from xgraph.algorithms.mst import prim_mst, kruskal_mst
from xgraph.graph import Graph


class TestMST(unittest.TestCase):
    def setUp(self) -> None:
        edges = [
            ('0', '1', 28),
            ('0', '5', 10),
            ('1', '2', 16),
            ('1', '6', 14),
            ('2', '3', 12),
            ('3', '4', 22),
            ('3', '6', 18),
            ('4', '5', 25),
            ('4', '6', 24),
        ]
        self.dummy_graph = Graph(vertices_num=7, edges=edges)
        self.filepath = r'../ga_tests/resources/graph.txt'
        self.edges, vert_num, _ = read_file(self.filepath)
        self.graph = Graph(vertices_num=vert_num, edges=self.edges)

    def test_prim_mst(self):
        mst = prim_mst(self.dummy_graph, representation='adj_list')
        self.assertEqual(99, mst.get('cost'))
        mst = prim_mst(self.dummy_graph, representation='inc_matrix')
        self.assertEqual(99, mst.get('cost'))

        mst = prim_mst(self.graph, representation='adj_list')
        self.assertEqual(21, mst.get('cost'))
        mst = prim_mst(self.graph, representation='inc_matrix')
        self.assertEqual(21, mst.get('cost'))

    def test_kruskal_mst(self):
        mst = kruskal_mst(self.dummy_graph, representation='adj_list')
        self.assertEqual(99, mst.get('cost'))
        mst = kruskal_mst(self.dummy_graph, representation='inc_matrix')
        self.assertEqual(99, mst.get('cost'))

        mst = kruskal_mst(self.graph, representation='adj_list')
        self.assertEqual(21, mst.get('cost'))
        mst = kruskal_mst(self.graph, representation='inc_matrix')
        self.assertEqual(21, mst.get('cost'))