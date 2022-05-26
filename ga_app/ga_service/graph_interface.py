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
            mst = prim_mst(self._graph, representation='adj_list')
            print('Prim\'s algorithm results using adjacency list')
            print('MST cost: {}, MST: {}'.format(mst.get('cost'), mst.get('mst')))
            mst = prim_mst(self._graph, representation='inc_matrix')
            print('Prim\'s algorithm results using incidence_matrix')
            print('MST cost: {}, MST: {}'.format(mst.get('cost'), mst.get('mst')))
        elif algorithm == 'kruskal':
            mst = kruskal_mst(self._graph, representation='adj_list')
            print('Kruskal\'s algorithm results using adjacency list')
            print('MST cost: {}, MST: {}'.format(mst.get('cost'), mst.get('mst')))
            mst = kruskal_mst(self._graph, representation='inc_matrix')
            print('Kruskal\'s algorithm results using incidence_matrix')
            print('MST cost: {}, MST: {}'.format(mst.get('cost'), mst.get('mst')))

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
                shortest_paths = dijkstra(self._digraph, start_vertex, representation='adj_list')
                print('Dijkstra\'s algorithm results using adjacency list')
                for vertex in sorted(shortest_paths.keys(), key=lambda v: v):
                    print('{} -> cost: {}, path: {}'.format(vertex, shortest_paths.get(vertex).get('cost'),
                                                            shortest_paths.get(vertex).get('path')))
                shortest_paths = dijkstra(self._digraph, start_vertex, representation='inc_matrix')
                print('Dijkstra\'s algorithm results using incidence_matrix')
                for vertex in sorted(shortest_paths.keys(), key=lambda v: v):
                    print('{} -> cost: {}, path: {}'.format(vertex, shortest_paths.get(vertex).get('cost'),
                                                            shortest_paths.get(vertex).get('path')))
            elif algorithm == 'bellman-ford':
                shortest_paths = bellman_ford(self._digraph, start_vertex, representation='adj_list')
                print('Bellman-Ford\'s algorithm results using adjacency list')
                for vertex in sorted(shortest_paths.keys(), key=lambda v: v):
                    print('{} -> cost: {}, path: {}'.format(vertex, shortest_paths.get(vertex).get('cost'),
                                                            shortest_paths.get(vertex).get('path')))
                shortest_paths = bellman_ford(self._digraph, start_vertex, representation='inc_matrix')
                print('Bellman-Ford\'s algorithm results using incidence_matrix')
                for vertex in sorted(shortest_paths.keys(), key=lambda v: v):
                    print('{} -> cost: {}, path: {}'.format(vertex, shortest_paths.get(vertex).get('cost'),
                                                            shortest_paths.get(vertex).get('path')))
        except NegativeWeightedGraphException:
            print('Graph contains negative weights, dijkstra algorithm is not applicable for such graphs')
        except DeadEndException:
            print('Starting vertex was interpreted as dead end')
        except VertexDoesNotExist:
            print('Starting vertex does not exist in graph')
        except Exception as e:
            print('[ERROR]: {}'.format(e))

    def print(self):
        print('========== Directed graph ==========')
        print('Adjacency list representation:')
        for vertex in sorted(self._digraph.adj_list.vertices, key=lambda v: v):
            print(self._digraph.adj_list.get_incident_vertices(vertex))
        print('Incidence matrix representation:')
        self._digraph.inc_matrix.print()
        print()
        print('========== Undirected graph ==========')
        print('Adjacency list representation:')
        for vertex in sorted(self._graph.adj_list.vertices, key=lambda v: v):
            print(self._graph.adj_list.get_incident_vertices(vertex))
        print('Incidence matrix representation:')
        self._graph.inc_matrix.print()

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
