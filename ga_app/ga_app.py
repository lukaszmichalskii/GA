from typing import Tuple, List

from ga_app.ga_service.graph_generator import GraphGenerator
from ga_app.ga_service.graph_interface import GraphInterface
from ga_app.ga_service.read_file import read_file


class GAApp:
    def __init__(self, filepath: str):
        self._filepath = filepath
        self._options = UserOptions()
        self._graph_interface = None
        self._graph_generator = GraphGenerator()
        self._app_flag = True
        self._help_msg = f"Available commands:\n{self._options.MST}\n{self._options.SPA}\n{self._options.RGEN}\n{self._options.WAR}"

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
        elif cmd == 'pmst' or cmd == 'prim_mst':
            self._graph_interface.minimum_spanning_tree(algorithm='prim')
        elif cmd == 'kmst' or cmd == 'kruskal_mst':
            self._graph_interface.minimum_spanning_tree(algorithm='kruskal')
        elif cmd == 'dsp' or cmd == 'dijkstra':
            start = input('start vertex = ')
            self._graph_interface.single_source_shortest_paths(start, algorithm='dijkstra')
        elif cmd == 'bfsp' or cmd == 'bellman-ford':
            start = input('start vertex = ')
            self._graph_interface.single_source_shortest_paths(start, algorithm='bellman-ford')
        elif cmd == 'rgen':
            v_num = input('V = ')
            try:
                v_num = int(v_num)
                directed = input('directed [y/n]? ')
                if directed == 'y' or directed == 'yes':
                    G = self._graph_generator.generate_graph(v_num, True)
                    self._graph_interface.digraph = G
                    self._graph_interface.print()
                else:
                    G = self._graph_generator.generate_graph(v_num, False)
                    self._graph_interface.graph = G
                    self._graph_interface.print()
            except TypeError or ValueError as e:
                print('[ERROR] invalid input, details: {}'.format(e))

        elif cmd == 'print' or cmd == 'p':
            self._graph_interface.print()
        elif cmd == 'help':
            print(self._help_msg)
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
    SPA = '[dsp, dijkstra_sp, bfsp, bellman-ford_sp: <-S start vertex>] - find single source shortest paths'
    RGEN = '[rgen: <-V vertices>] - generate new random graph with V nodes and replace current'
    WAR = '[IMPORTANT]: all commands are sensitive case which means "RGEN" or "rGen" command will not work'


class InitializationFailed(Exception):
    pass
