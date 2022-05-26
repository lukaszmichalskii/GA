from typing import List, Tuple

from xgraph.data_structures.adjacency_list import AdjacencyList
from xgraph.data_structures.incidence_matrix import IncidenceMatrix


class DiGraph:
    def __init__(self, vertices_num: int, edges: List[Tuple[str, str, int]]):
        self._directed = True
        self._adj_list = AdjacencyList(edges, vertices_num, self._directed)
        self._inc_matrix = IncidenceMatrix(edges, vertices_num, self._directed)

    @property
    def adj_list(self) -> AdjacencyList:
        return self._adj_list

    @property
    def inc_matrix(self) -> IncidenceMatrix:
        return self._inc_matrix

    @property
    def vertices(self) -> List[str]:
        return self.inc_matrix.vertices

    @property
    def is_directed(self):
        return self._directed
