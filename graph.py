class Graph:
    adj_list = {}
    type = "!directed"
    nodes_list = []

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
        try:
            fin = open(filename, encoding="utf8")
        except FileNotFoundError:
            print("ERROR: No such file or directory")
            return False

        type = fin.readline()
        n, m = map(int, fin.readline().split())
        self.nodes_list = fin.readline().split()
        edges = fin.readlines()

        for edge in edges:
            v, u = edge.split()

            if v not in adj_list.keys():
                adj_list[v] = []
            adj_list[v].append(u)

            if type != "directed":
                if u not in adj_list.keys():
                    adj_list[u] = []
                adj_list[u].append(v)
        if len(adj_list.keys()) != n:
            for node in self.nodes_list:
                if node not in adj_list.keys():
                    adj_list[node] = []
        self.adj_list = adj_list
        return True

    def copy(self):
        pass

    def add_node(self, node):
        self.adj_list[node] = []
        self.nodes_list.append(node)

    def add_edge(self, edge):
        v, u = edge[0], edge[1]
        try:
            self.adj_list[v].append(u)
        except KeyError:
            print(f"Unable to add the edge. No such vertex {v}")
            return False

        if type != "directed":
            try:
                self.adj_list[u].append(v)
            except KeyError:
                print(f"Unable to add the edge. No such vertex {u}")
                return False
        return True

    def delete_node(self, node):
        try:
            for item in self.adj_list.items():
                if node in item[1]:
                    del self.adj_list[item[0]][self.adj_list[item[0]].index(node)]
            del self.adj_list[node]
            del self.nodes_list[self.nodes_list.index(node)]
        except KeyError:
            print(f"ERROR: No such vertex {node}")
            return False
        return True

    def delete_edge(self, edge):
        v, u = edge[0], edge[1]

        try:
            del self.adj_list[v][(self.adj_list[v]).index(u)]
        except KeyError:
            print(f"ERROR: No such edge ({v}, {u})")
            return False

        if type != "directed":
            try:
                del self.adj_list[u][(self.adj_list[u]).index(v)]
            except KeyError:
                print(f"ERROR: No such edge ({v}, {u})")
                return False
        return True

    def print_to_file(self, filename):
        try:
            fout = open(filename, 'w', encoding="utf8")
        except FileNotFoundError:
            print("ERROR: No such file or directory")
            return False
        lst = self.create_edge_list()
        print(self.type, file=fout)
        print(len(self.nodes_list), len(lst), file=fout)
        for edge in lst:
            print(f"{edge[0]} {edge[1]}", file=fout)
        return True

    def print_to_console(self):
        print(self.adj_list)


