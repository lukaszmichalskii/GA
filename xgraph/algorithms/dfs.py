from typing import Set, Union

from xgraph.digraph import DiGraph
from xgraph.graph import Graph


def depth_first_search(graph: Union[DiGraph, Graph], vertex: str) -> Set[str]:
    dfs = set()
    _dfs(dfs, graph, vertex)
    return dfs


def _dfs(visited: Set[str], graph: Union[DiGraph, Graph], vertex: str) -> None:
    if vertex not in visited:
        visited.add(vertex)
        for adj_vertex, _ in graph.adj_list.get_incident_vertices(vertex):
            _dfs(visited, graph, adj_vertex)
