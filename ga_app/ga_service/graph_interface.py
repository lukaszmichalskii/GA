from typing import List, Tuple

from xgraph import digraph
from xgraph.algorithms.mst import prim_mst, kruskal_mst
from xgraph.algorithms.shortest_paths import dijkstra, bellman_ford
from xgraph.digraph import DiGraph
from xgraph.graph import Graph


class GraphInterface:
    def __init__(self, vertices_num, edges_list: List[Tuple[str, str, int]]):
        self._graph = Graph(vertices_num, edges_list)
        self._digraph = DiGraph(vertices_num, edges_list)

    def minimum_spanning_tree(self, algorithm: str):
        print('Minimum-spanning tree algorithm:')
        if algorithm == 'prim':
            self._run_prim_mst(representation='adj_list')
            self._run_prim_mst(representation='inc_matrix')
        elif algorithm == 'kruskal':
            self._run_kruskal_mst(representation='adj_list')
            self._run_kruskal_mst(representation='inc_matrix')

    def single_source_shortest_paths(self, start_vertex: str, algorithm: str):
        try:
            if start_vertex not in self._digraph.vertices:
                print(self._digraph.vertices)
                raise VertexDoesNotExist
            if not self._digraph.adj_list.get_incident_vertices(start_vertex):
                raise DeadEndException
            if algorithm == 'dijkstra':
                if self._digraph.has_negative_weights():
                    raise NegativeWeightedGraphException
                self._run_dijkstra(start_vertex, representation='adj_list')
                self._run_dijkstra(start_vertex, representation='inc_matrix')
            elif algorithm == 'bellman-ford':
                if self._digraph.has_negative_weights():
                    print('[WARNING]: algorithm run using adjacency list')
                    self._run_bellman_ford(start_vertex, representation='adj_list')
                    return
                self._run_bellman_ford(start_vertex, representation='adj_list')
                self._run_bellman_ford(start_vertex, representation='inc_matrix')
        except NegativeWeightedGraphException:
            print('Graph contains negative weights, dijkstra algorithm is not applicable for such graphs')
        except DeadEndException:
            print('Starting vertex was interpreted as dead end')
        except VertexDoesNotExist:
            print('Starting vertex does not exist in graph')
        except Exception as e:
            print('[ERROR]: {}'.format(e))

    def print(self):
        print('========== DIRECTED GRAPH ==========')
        print('Adjacency list representation:')
        for vertex in sorted(self._digraph.adj_list.vertices, key=lambda v: v):
            print(self._digraph.adj_list.get_incident_vertices(vertex))
        print('Incidence matrix representation:')
        self._digraph.inc_matrix.print()
        print()
        print('========== UNDIRECTED GRAPH ==========')
        print('Adjacency list representation:')
        for vertex in sorted(self._graph.adj_list.vertices, key=lambda v: v):
            print(self._graph.adj_list.get_incident_vertices(vertex))
        print('Incidence matrix representation:')
        self._graph.inc_matrix.print()

    def _run_prim_mst(self, representation: str):
        mst = prim_mst(self._graph, representation=representation)
        print(f'Prim\'s algorithm results using {representation}')
        print('MST cost: {}, MST: {}'.format(mst.get('cost'), mst.get('mst')))

    def _run_kruskal_mst(self, representation: str):
        mst = kruskal_mst(self._graph, representation=representation)
        print(f'Kruskal\'s algorithm results using {representation}')
        print('MST cost: {}, MST: {}'.format(mst.get('cost'), mst.get('mst')))

    def _run_bellman_ford(self, start_vertex: str, representation: str):
        shortest_paths = bellman_ford(self._digraph, start_vertex, representation=representation)
        print(f'Bellman-Ford\'s algorithm results using {representation}')
        for vertex in sorted(shortest_paths.keys(), key=lambda v: v):
            print('{} -> cost: {}, path: {}'.format(vertex, shortest_paths.get(vertex).get('cost'),
                                                    shortest_paths.get(vertex).get('path')))

    def _run_dijkstra(self, start_vertex: str, representation: str):
        shortest_paths = dijkstra(self._digraph, start_vertex, representation=representation)
        print(f'Dijkstra\'s algorithm results using {representation}')
        for vertex in sorted(shortest_paths.keys(), key=lambda v: v):
            print('{} -> cost: {}, path: {}'.format(vertex, shortest_paths.get(vertex).get('cost'),
                                                    shortest_paths.get(vertex).get('path')))

    @property
    def digraph(self):
        return self._digraph

    @digraph.setter
    def digraph(self, digraph: DiGraph):
        self._digraph = digraph

    @property
    def graph(self):
        return self._graph

    @graph.setter
    def graph(self, graph: Graph):
        self._graph = graph


class VertexDoesNotExist(Exception):
    pass


class DeadEndException(Exception):
    pass


class NegativeWeightedGraphException(Exception):
    pass
