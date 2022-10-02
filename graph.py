class Graph:
    adj_list = {}

    def __init__(self):
        self.adj_list = {}

    def create_edge_list(self):
        edge_list = []

        for node in self.adj_list.keys():
            for adj in self.adj_list[node]:
                edge_list.append((node, adj))

        return edge_list

    def create_from_file(self, filename):
        adj_list = {}
        fin = open(filename, encoding="utf8")

        type = fin.readline()
        n, m = map(int, fin.readline().split())
        edges = fin.readlines()

        for edge in edges:
            v, u = map(int, edge.split())

            if v not in adj_list.keys():
                adj_list[v] = []
            adj_list[v].append(u)

            if type != "directed":
                if u not in adj_list.keys():
                    adj_list[u] = []
                adj_list[u].append(v)

        self.adj_list = adj_list

    def copy(self):
        pass

    def add_node(self, node):
        pass

    def add_edge(self, edge):
        pass

    def delete_node(self, node):
        pass

    def delete_edge(self, edge):
        pass

    def print_to_file(self, filename):
        fout = open(filename, 'w', encoding="utf8")

    def print_to_console(self):
        print(self.adj_list)


