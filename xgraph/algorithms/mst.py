from typing import Dict, Union, List, Tuple

from xgraph.data_structures.edge import Edge
from xgraph.data_structures.heap import HeapAdjVertices, HeapEdges
from xgraph.graph import Graph


def prim_mst(graph: Graph, representation: str) -> Dict[str, Union[List[Tuple[str, int]], int]]:
    mst, visited, edges, cost = list(), list(), HeapAdjVertices(), 0
    vertex = graph.vertices[0]
    visited.append(vertex)
    while len(mst) < len(graph.vertices) - 1:
        if representation == 'adj_list':
            adj_vertices = [adj_vertex for adj_vertex in graph.adj_list.get_incident_vertices(vertex) if adj_vertex[0] not in visited]
        else:
            adj_vertices = [adj_vertex for adj_vertex in graph.inc_matrix.get_incident_vertices(vertex) if adj_vertex[0] not in visited]
        edges.add_all(adj_vertices)
        edge = edges.remove()
        visited.append(edge[0])
        cost += edge[1]
        mst.append((vertex, edge[0]))
        vertex = visited[-1]

    return {'mst': mst, 'cost': cost}


def kruskal_mst(graph: Graph, representation: str) -> Dict[str, Union[List[Tuple[str, str]], int]]:
    vertices_colors = [i for i in range(len(graph.vertices))]
    mst, visited, cost, edges = list(), list(), 0, HeapEdges()
    if representation == 'adj_list':
        edges.add_all(graph.adj_list.get_edges_collection())
    else:
        edges.add_all(graph.inc_matrix.get_edges_collection())
    while len(mst) < len(graph.vertices) - 1:
        edge: Edge = edges.remove()
        if edge.source not in visited and edge.dest not in visited:
            vertices_colors[int(edge.dest)] = vertices_colors[int(edge.source)]
            mst.append((edge.source, edge.dest))
            visited.extend([edge.source, edge.dest])
            cost += edge.weight
        elif edge.source in visited and edge.dest not in visited:
            vertices_colors[int(edge.dest)] = vertices_colors[int(edge.source)]
            mst.append((edge.source, edge.dest))
            visited.append(edge.dest)
            cost += edge.weight
        elif edge.source not in visited and edge.dest in visited:
            vertices_colors[int(edge.source)] = vertices_colors[int(edge.dest)]
            mst.append((edge.source, edge.dest))
            visited.append(edge.source)
            cost += edge.weight
        elif edge.source in visited and edge.dest in visited and vertices_colors[int(edge.source)] != vertices_colors[int(edge.dest)]:
            sub_tree_color = vertices_colors[int(edge.dest)]
            for sub_tree_vertex in visited:
                if vertices_colors[int(sub_tree_vertex)] == sub_tree_color:
                    vertices_colors[int(sub_tree_vertex)] = vertices_colors[int(edge.source)]
            mst.append((edge.source, edge.dest))
            cost += edge.weight

    return {'mst': mst, 'cost': cost}