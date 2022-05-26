from typing import Tuple, List

from ga_app.ga_service.graph_interface import GraphInterface
from ga_app.ga_service.read_file import read_file


class GAApp:
    def __init__(self, filepath: str):
        self._filepath = filepath
        self._options = UserOptions()
        self._graph_interface = None
        self._app_flag = True
        self._help_msg = f"Available commands:\n{self._options.MST}\n{self._options.SPA}"

    def run(self):
        edges, vertices_num = self._load_edges()
        self._graph_interface = GraphInterface(vertices_num, edges)
        print('Initialization successful')
        self._run_cli()

    def _run_cli(self):
        while self._app_flag:
            cmd = input('>')
            self._handle_user_cmd(cmd)

    def _handle_user_cmd(self, cmd: str) -> None:
        if cmd == 'exit' or cmd == 'quit':
            self._app_flag = False
            return
        elif cmd == 'print' or cmd == 'p':
            self._graph_interface.print()
            return
        elif cmd == 'help':
            print(self._help_msg)
            return
        else:
            print(f'warning: "{cmd}" command not found, "help" for command list')

    def _load_edges(self) -> Tuple[List[Tuple[str, str, int]], int]:
        try:
            edges, vertices_num, _ = read_file(self._filepath)
            return edges, vertices_num
        except Exception:
            raise InitializationFailed


class UserOptions:
    MST = '[pmst, prim_mst, kmst, kruskal_mst] - find minimum-spanning-tree of graph'
    SPA = '[dsp, dijkstra_sp, bfsp, bellman-ford_sp] - find single source shortest paths'
    RGEN = '[rgen, re-generate_graph] - generate new random graph and replace current'


class InitializationFailed(Exception):
    pass
