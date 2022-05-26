from typing import List, Tuple

from xgraph.graph_utils import adj_list_from_edges, inc_matrix_from_edges


class DiGraph:
    def __init__(self, vertices_num: int, edges: List[Tuple[str, str, int]]):
        self._directed = True
        self._adj_list = adj_list_from_edges(edges, self._directed)
        self._inc_matrix = inc_matrix_from_edges(edges, vertices_num, self._directed)

    @property
    def adj_list(self):
        return self._adj_list

    @property
    def inc_matrix(self):
        return self._inc_matrix
