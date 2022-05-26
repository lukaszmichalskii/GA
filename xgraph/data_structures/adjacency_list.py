from typing import Dict, List, Tuple

from xgraph.data_structures.edge import Edge


class AdjacencyList:
    def __init__(self, edges: List[Tuple[str, str, int]], vertices_num: int, directed: bool):
        self._adj_list: Dict[str, List[Tuple[str, int]]] = adj_list_from_edges(edges, vertices_num, directed)

    def get_incident_vertices(self, vertex: str) -> List[Tuple[str, int]]:
        return self._adj_list[vertex]

    def get_edges_collection(self) -> List[Edge]:
        edges = list()
        for vertex in self._adj_list.keys():
            for adj_vertex in self._adj_list[vertex]:
                edges.append(Edge((vertex, adj_vertex[0], adj_vertex[1])))
        return edges

    @property
    def vertices(self) -> List[str]:
        return list(self._adj_list.keys())


def adj_list_from_edges(edges: List[Tuple[str, str, int]], vertices_num: int, directed: bool) -> Dict[str, List[Tuple[str, int]]]:
    adj_list = _directed_from_edges_adj_list(edges, vertices_num) if directed else _undirected_from_edges_adj_list(edges, vertices_num)
    _dont_skip_islands(vertices_num, adj_list)
    return adj_list


def _directed_from_edges_adj_list(edges: List[Tuple[str, str, int]], vertices_num: int) -> Dict[str, List[Tuple[str, int]]]:
    adj_list: Dict[str, List[Tuple[str, int]]] = dict()
    if edges is None:
        raise TypeError
    for source, dest, weight in edges:
        if source in adj_list and dest not in adj_list:
            adj_list[source].append((dest, weight))
            adj_list[dest] = list()
        elif source in adj_list:
            adj_list[source].append((dest, weight))
        else:
            adj_list[source] = [(dest, weight)]
            adj_list[dest] = list()

    return adj_list


def _undirected_from_edges_adj_list(edges: List[Tuple[str, str, int]], vertices_num: int) -> Dict[str, List[Tuple[str, int]]]:
    if len(set(edges)) != len(edges):
        raise EdgeOverrideException
    adj_list: Dict[str, List[Tuple[str, int]]] = dict()
    if edges is None:
        raise TypeError
    for source, dest, weight in edges:
        if source in adj_list and dest in adj_list:
            adj_list[source].append((dest, weight))
            adj_list[dest].append((source, weight))
        elif source in adj_list and dest not in adj_list:
            adj_list[source].append((dest, weight))
            adj_list[dest] = [(source, weight)]
        elif source not in adj_list and dest in adj_list:
            adj_list[dest].append((source, weight))
            adj_list[source] = [(dest, weight)]
        else:
            adj_list[source] = [(dest, weight)]
            adj_list[dest] = [(source, weight)]

    if vertices_num != len(list(adj_list.keys())):
        for v in range(vertices_num):
            if str(v) not in adj_list.keys():
                adj_list[str(v)] = list()
    return adj_list


def _dont_skip_islands(vertices_num: int, adj_list: Dict[str, List[Tuple[str, int]]]) -> None:
    if vertices_num == len(list(adj_list.keys())):
        return
    for v in range(vertices_num):
        if str(v) not in adj_list.keys():
            adj_list[str(v)] = list()


class EdgeOverrideException(Exception):
    pass
