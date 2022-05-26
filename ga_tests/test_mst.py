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
        edges2 = [
            ('0', '3', 6),
            ('0', '4', 6),
            ('1', '2', 4),
            ('1', '4', 9),
            ('1', '5', 3),
            ('3', '4', 2),
        ]

        edges3 = [
            ('0', '3', 9),
            ('0', '4', 4),
            ('0', '6', 3),
            ('1', '3', 4),
            ('1', '4', 2),
            ('2', '4', 3),
            ('3', '4', 8),
            ('5', '6', 1)
        ]
        self.dummy_graph = Graph(vertices_num=7, edges=edges)
        self.dummy_graph2 = Graph(vertices_num=6, edges=edges2)
        self.dummy_graph3 = Graph(vertices_num=7, edges=edges3)
        self.filepath = r'../ga_tests/resources/graph.txt'
        self.edges, vert_num, _ = read_file(self.filepath)
        self.graph = Graph(vertices_num=vert_num, edges=self.edges)
        self.filepath = r'../ga_tests/resources/graph_updated.txt'
        self.edges2, vert_num2, _ = read_file(self.filepath)
        self.graph2 = Graph(vertices_num=vert_num2, edges=self.edges2)

    def test_prim_mst(self):
        mst = prim_mst(self.dummy_graph, representation='adj_list')
        self.assertEqual(99, mst.get('cost'))
        mst = prim_mst(self.dummy_graph, representation='inc_matrix')
        self.assertEqual(99, mst.get('cost'))

        mst = prim_mst(self.graph, representation='adj_list')
        self.assertEqual(21, mst.get('cost'))
        mst = prim_mst(self.graph, representation='inc_matrix')
        self.assertEqual(21, mst.get('cost'))

        mst = prim_mst(self.dummy_graph2, representation='adj_list')
        self.assertEqual(24, mst.get('cost'))
        mst = prim_mst(self.dummy_graph2, representation='inc_matrix')
        self.assertEqual(24, mst.get('cost'))

        mst = prim_mst(self.graph2, representation='adj_list')
        self.assertEqual(20, mst.get('cost'))
        mst = prim_mst(self.graph2, representation='inc_matrix')
        self.assertEqual(20, mst.get('cost'))

        mst = prim_mst(self.dummy_graph3, representation='adj_list')
        self.assertEqual(17, mst.get('cost'))
        mst = prim_mst(self.dummy_graph3, representation='inc_matrix')
        self.assertEqual(17, mst.get('cost'))

    def test_kruskal_mst(self):
        mst = kruskal_mst(self.dummy_graph, representation='adj_list')
        self.assertEqual(99, mst.get('cost'))
        mst = kruskal_mst(self.dummy_graph, representation='inc_matrix')
        self.assertEqual(99, mst.get('cost'))

        mst = kruskal_mst(self.graph, representation='adj_list')
        self.assertEqual(21, mst.get('cost'))
        mst = kruskal_mst(self.graph, representation='inc_matrix')
        self.assertEqual(21, mst.get('cost'))

        mst = kruskal_mst(self.dummy_graph2, representation='adj_list')
        self.assertEqual(24, mst.get('cost'))
        mst = kruskal_mst(self.dummy_graph2, representation='inc_matrix')
        self.assertEqual(24, mst.get('cost'))

        mst = kruskal_mst(self.dummy_graph3, representation='adj_list')
        self.assertEqual(17, mst.get('cost'))
        mst = kruskal_mst(self.dummy_graph3, representation='inc_matrix')
        self.assertEqual(17, mst.get('cost'))
