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
            self._handle_generation_process()
        elif cmd == 'load' or cmd == 'reload':
            self._handle_reload_process()
        elif cmd == 'print' or cmd == 'p':
            self._graph_interface.print()
        elif cmd == 'help':
            print(self._options.help_msg())
        else:
            print(f'warning: "{cmd}" command not found, "help" for command list')

    def _load_edges(self) -> Tuple[List[Tuple[str, str, int]], int]:
        try:
            edges, vertices_num, _ = read_file(self._filepath)
            return edges, vertices_num
        except Exception:
            raise InitializationFailed

    def _handle_generation_process(self):
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

    def _handle_reload_process(self):
        is_new = input('reload graph from filepath: {} [y/n]?'.format(self._filepath))
        if is_new == 'y' or is_new == 'yes':
            edges, V = self._load_edges()
            self._graph_interface.graph = GraphGenerator.generate_graph_from_edges(V, edges)
            self._graph_interface.digraph = GraphGenerator.generate_digraph_from_edges(V, edges)
            return
        filepath = input('filepath = ')
        try:
            edges, V, _ = read_file(filepath)
            self._graph_interface.graph = GraphGenerator.generate_graph_from_edges(V, edges)
            self._graph_interface.digraph = GraphGenerator.generate_digraph_from_edges(V, edges)
            return
        except Exception as e:
            print('[ERROR] failed to load graph, details: {}'.format(e))


class UserOptions:
    def __init__(self):
        self.MST = '[pmst, prim_mst, kmst, kruskal_mst] - find minimum-spanning-tree of graph'
        self.SPA = '[dsp, dijkstra_sp, bfsp, bellman-ford_sp: <-S start vertex>] - find single source shortest paths'
        self.RGEN = '[rgen: <-V vertices>] - generate new random graph with V nodes and replace current'
        self.LOAD = '[load, reload: [-F filepath] - reload graph from predefined filepath or load from different file'
        self.WAR = '[IMPORTANT]: all commands are sensitive case which means "RGEN" or "rGen" command will not work'

    def help_msg(self) -> str:
        return f"Available commands:\n" \
               f"{self.MST}\n" \
               f"{self.SPA}\n" \
               f"{self.RGEN}\n" \
               f"{self.LOAD}\n" \
               f"{self.WAR}"


class InitializationFailed(Exception):
    pass
