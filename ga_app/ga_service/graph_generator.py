import random
from typing import Tuple, List, Union

import networkx.generators

from ga_app.ga_service.gg_settings import GraphGeneratorSettings
from xgraph.digraph import DiGraph
from xgraph.graph import Graph


class GraphGenerator:
    def __init__(self):
        self._gg_settings = GraphGeneratorSettings()

    def generate_graph(self, V, directed: bool) -> Union[Graph, DiGraph]:
        E = self.generate_edges_collection(V, directed)
        return DiGraph(V, E) if directed else Graph(V, E)

    def generate_edges_collection(self, V, directed: bool) -> List[Tuple[str, str, int]]:
        G = networkx.generators.gnp_random_graph(V, self._gg_settings.probability, directed)
        E = list()
        for edge in G.edges.data():
            E.append((str(edge[0]), str(edge[1]),
                      random.randrange(self._gg_settings.weights_interval[0], self._gg_settings.weights_interval[1])))
        E.sort(key=lambda edge: edge[0])
        return E
