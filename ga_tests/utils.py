from typing import List, Tuple, Union, Set

from xgraph.digraph import DiGraph
from xgraph.graph import Graph


def is_heap(array: List[Tuple[str, int]]):
    if len(array) <= 1:
        return True
    for i in range((len(array) - 2) // 2 + 1):
        if array[i][1] > array[2 * i + 1][1] or (2 * i + 2 != len(array) and array[i][1] > array[2 * i + 2][1]):
            return False
    return True


def depth_first_search(graph: Union[DiGraph, Graph], vertex: str) -> Set[str]:
    dfs = set()
    _dfs(dfs, graph, vertex)
    return dfs


def _dfs(visited: Set[str], graph: Union[DiGraph, Graph], vertex: str) -> None:
    if vertex not in visited:
        print(vertex)
        visited.add(vertex)
        for adj_vertex, _ in graph.adj_list.get_incident_vertices(vertex):
            _dfs(visited, graph, adj_vertex)
