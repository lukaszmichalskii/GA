from typing import Dict, Union, List

from xgraph.data_structures.heap import HeapAdjVertices
from xgraph.digraph import DiGraph


def dijkstra(graph: DiGraph, start: str, representation: str) -> Dict[str, Dict[str, Union[int, float, str]]]:
    shortest_paths: Dict[str, Dict[str, Union[int, List[str]]]] = dict()
    visited, heap = list(), HeapAdjVertices()
    for vertex in graph.vertices:
        shortest_paths[vertex] = {'cost': float('inf'), 'path':''}
    shortest_paths[start] = {'cost': 0, 'path': 'start'}
    heap.add((start, shortest_paths[start]['path']))

    while len(visited) < len(graph.vertices):
        if heap.size <= 0:
            return shortest_paths
        start = heap.remove()[0]
        if representation == 'adj_list':
            adj_vertices = graph.adj_list.get_incident_vertices(start)
        else:
            adj_vertices = graph.inc_matrix.get_incident_vertices(start)
        for adj_vertex in adj_vertices:
            if shortest_paths[start]['cost'] + adj_vertex[1] < shortest_paths[adj_vertex[0]]['cost'] and adj_vertex[0] not in visited:
                shortest_paths[adj_vertex[0]]['cost'] = shortest_paths[start]['cost'] + adj_vertex[1]
                shortest_paths[adj_vertex[0]]['path'] = start
                heap.add((adj_vertex[0], shortest_paths[adj_vertex[0]]['cost']))

        visited.append(start)

    return shortest_paths


def bellman_ford(graph: DiGraph, start: str, representation: str) -> Dict[str, Dict[str, Union[int, float, str]]]:
    shortest_paths, edges = dict(), list()
    for vertex in graph.vertices:
        shortest_paths[vertex] = {'cost': float('inf'), 'path': ''}
    shortest_paths[start] = {'cost': 0, 'path': 'start'}

    if representation == 'adj_list':
        edges = graph.adj_list.get_edges_collection()
    else:
        edges = graph.inc_matrix.get_edges_collection()
    iteration = 0
    while iteration < len(graph.vertices) - 1:
        relaxation = 0
        for edge in edges:
            if shortest_paths[edge.source]['cost'] + edge.weight < shortest_paths[edge.dest]['cost']:
                shortest_paths[edge.dest]['cost'] = shortest_paths[edge.source]['cost'] + edge.weight
                shortest_paths[edge.dest]['path'] = edge.source
                relaxation += 1
        iteration += 1
        if relaxation == 0:
            break

    return shortest_paths
