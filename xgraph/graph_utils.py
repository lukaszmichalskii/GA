from typing import List, Tuple, Dict

from xgraph.data_structures.edge import Edge


def adj_list_from_edges(edges: List[Tuple[str, str, int]], directed: bool) -> Dict[str, List[Tuple[str, int]]]:
    return _directed_from_edges_adj_list(edges) if directed else _undirected_from_edges_adj_list(edges)


def _directed_from_edges_adj_list(edges: List[Tuple[str, str, int]]) -> Dict[str, List[Tuple[str, int]]]:
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


def _undirected_from_edges_adj_list(edges: List[Tuple[str, str, int]]):
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

    return adj_list


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


def _edges_collection(edges: List[Tuple[str, str, int]]) -> List[Edge]:
    return [Edge(edge) for edge in edges]


class EdgeOverrideException(Exception):
    pass
