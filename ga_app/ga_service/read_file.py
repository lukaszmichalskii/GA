from typing import List, Tuple


def read_file(filepath: str):
    edges: List[Tuple[str, str, int]] = []
    try:
        with open(filepath, 'r') as file:
            line: str = file.readline()
            info: List[str] = line.split(' ')
            edges_num, vertices_num = int(info[0]), int(info[1])
            for i in range(edges_num):
                line = file.readline()
                info = line.split(' ')
                edges.append((info[0], info[1], int(info[2])))
        return edges, int(vertices_num), int(edges_num)
    except Exception as e:
        raise e
