from typing import Tuple


class Edge:
    def __init__(self, edge: Tuple[str, str, int]):
        self.__source = edge[0]
        self.__dest = edge[1]
        self.__weight = edge[2]

    def __str__(self):
        return str((self.__source, self.__dest, self.__weight))

    def __eq__(self, other):
        if isinstance(other, Edge):
            return self.__source == other.source and self.__dest == other.dest and self.__weight == other.weight
        return False

    def reverse(self):
        return Edge((self.__dest, self.__source, self.__weight))

    @property
    def source(self):
        return self.__source

    @property
    def dest(self):
        return self.__dest

    @property
    def weight(self):
        return self.__weight
