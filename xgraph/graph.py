from typing import Tuple, List

from xgraph.graph_utils import adj_list_from_edges, inc_matrix_from_edges


class Graph:
    def __init__(self, vertices_num: int, edges: List[Tuple[str, str, int]]):
        self._directed = False
        self._adj_list = adj_list_from_edges(edges, self._directed)
        self._inc_matrix = inc_matrix_from_edges(edges, vertices_num, self._directed)

    @property
    def adj_list(self):
        return self._adj_list

    @property
    def inc_matrix(self):
        return self._inc_matrix

    @property
    def vertices(self):
        return list(self._adj_list.keys())

    @property
    def is_directed(self):
        return self._directed

    def get_incident_vertices_to_vertex_from_inc_matrix(self, vertex: str) -> List[Tuple[str, int]]:
        incident_vertices = list()
        for e_num in range(len(self._inc_matrix[int(vertex)])):
            if self._inc_matrix[int(vertex)][e_num] != 0:
                for v_num in range(len(self._inc_matrix)):
                    if self._inc_matrix[int(vertex)][e_num] == self._inc_matrix[v_num][e_num] and v_num != int(vertex):
                        incident_vertices.append((str(v_num), self._inc_matrix[int(vertex)][e_num]))
        return incident_vertices
