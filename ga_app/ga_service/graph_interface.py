from typing import List, Tuple

from xgraph.digraph import DiGraph
from xgraph.graph import Graph


class GraphInterface:
    def __init__(self, vertices_num, edges_list: List[Tuple[str, str, int]]):
        self._graph = Graph(vertices_num, edges_list)
        self._digraph = DiGraph(vertices_num, edges_list)

    def print(self):
        print('========== Directed graph ==========')
        print('Adjacency list representation:')
        for vertex in sorted(self._graph.adj_list.keys(), key=lambda v: v):
            print(self._digraph.adj_list[vertex])
        print('Incidence matrix representation:')
        for vertex in self._digraph.inc_matrix:
            print(vertex)

        print('========== Undirected graph ==========')
        print('Adjacency list representation:')
        for vertex in sorted(self._graph.adj_list.keys(), key=lambda v: v):
            print(self._graph.adj_list[vertex])
        print('Incidence matrix representation:')
        for vertex in self._graph.inc_matrix:
            print(vertex)
