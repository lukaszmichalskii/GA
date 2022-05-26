from typing import List, Tuple

from xgraph.data_structures.edge import Edge


class IncidenceMatrix:
    def __init__(self, edges: List[Tuple[str, str, int]], vertices_num: int, directed: bool):
        self._directed = directed
        self._inc_matrix: List[List[int]] = inc_matrix_from_edges(edges, vertices_num, self._directed)
        self._vertices = [str(vertex) for vertex in range(len(self._inc_matrix))]

    def get_incident_vertices(self, vertex: str) -> List[Tuple[str, int]]:
        incident_vertices = list()
        if self._directed:
            for e_num in range(len(self._inc_matrix[int(vertex)])):
                if self._inc_matrix[int(vertex)][e_num] != 0:
                    for v_num in range(len(self._inc_matrix)):
                        if self._inc_matrix[int(vertex)][e_num] == -self._inc_matrix[v_num][e_num] and \
                                self._inc_matrix[int(vertex)][e_num] > 0:
                            incident_vertices.append((str(v_num), self._inc_matrix[int(vertex)][e_num]))
            return incident_vertices
        for e_num in range(len(self._inc_matrix[int(vertex)])):
            if self._inc_matrix[int(vertex)][e_num] != 0:
                for v_num in range(len(self._inc_matrix)):
                    if self._inc_matrix[int(vertex)][e_num] == self._inc_matrix[v_num][e_num] and v_num != int(vertex):
                        incident_vertices.append((str(v_num), self._inc_matrix[int(vertex)][e_num]))
        return incident_vertices

    def get_edges_collection(self) -> List[Edge]:
        edges = list()
        if self._directed:
            for v_num in range(len(self._inc_matrix)):
                for e_num in range(len(self._inc_matrix[v_num])):
                    if self._inc_matrix[v_num][e_num] != 0:
                        for i in range(len(self._inc_matrix)):
                            if i == v_num:
                                continue
                            if self._inc_matrix[v_num][e_num] == -self._inc_matrix[i][e_num] and self._inc_matrix[v_num][e_num] > 0:
                                edges.append(Edge((str(v_num), str(i), self._inc_matrix[v_num][e_num])))
            return edges
        for v_num in range(len(self._inc_matrix)):
            for e_num in range(len(self._inc_matrix[v_num])):
                if self._inc_matrix[v_num][e_num] != 0:
                    for i in range(len(self._inc_matrix)):
                        if i == v_num:
                            continue
                        if self._inc_matrix[v_num][e_num] == self._inc_matrix[i][e_num] and v_num < i:
                            edges.append(Edge((str(v_num), str(i), self._inc_matrix[v_num][e_num])))
        return edges

    @property
    def vertices(self) -> List[str]:
        return self._vertices


def inc_matrix_from_edges(edges: List[Tuple[str, str, int]], vertices_num, directed: bool) -> List[List[int]]:
    inc_matrix = _create_empty_inc_matrix(vertices_num, len(edges))
    if directed:
        _directed_from_edges_inc_matrix(inc_matrix, edges)
    else:
        _undirected_from_edges_inc_matrix(inc_matrix, edges)
    return inc_matrix


def _create_empty_inc_matrix(vertices_number: int, edges_number: int) -> List[List[int]]:
    inc_matrix = [0] * vertices_number
    for vertex in range(vertices_number):
        inc_matrix[vertex] = [0] * edges_number
    return inc_matrix


def _directed_from_edges_inc_matrix(inc_matrix: List[List[int]], edges: List[Tuple[str, str, int]]):
    for i in range(len(edges)):
        inc_matrix[int(edges[i][0])][i] = int(edges[i][2])
        inc_matrix[int(edges[i][1])][i] = int(-edges[i][2])
    return inc_matrix


def _undirected_from_edges_inc_matrix(inc_matrix: List[List[int]], edges: List[Tuple[str, str, int]]):
    for i in range(len(edges)):
        inc_matrix[int(edges[i][0])][i] = int(edges[i][2])
        inc_matrix[int(edges[i][1])][i] = int(edges[i][2])
    return inc_matrix
