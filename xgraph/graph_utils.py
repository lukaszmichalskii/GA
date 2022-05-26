from typing import List, Tuple

from xgraph.data_structures.edge import Edge


def edges_collection(edges: List[Tuple[str, str, int]]) -> List[Edge]:
    return [Edge(edge) for edge in edges]
