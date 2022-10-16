class Graph:
    adj_list = {}
    type = "!directed"
    weighted = False
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

        self.type = fin.readline().split()[0]
        self.weighted = True if fin.readline().split()[0] == "weighted" else False
        n, m = map(int, fin.readline().split())
        self.nodes_list = fin.readline().split()

        for node in self.nodes_list:
                adj_list[node] = []

        edges = fin.readlines()
        for edge in edges:
            v, u, c = edge.split()
            try:
                if v == u and self.type == "!directed":
                    print(f"ERROR: No loop in not directed graph")
                    return False
                if u in self.nodes_list:
                    if u not in adj_list[v]:
                        adj_list[v].append([u, c])
                    else:
                        print(f"ERROR: No multiple edges")
                        return False
                else:
                    print(f"ERROR: No such vertex {u}")
                    return False
            except KeyError:
                print(f"ERROR: No such vertex {v}")
                return False

            if self.type == "!directed":
                try:
                    if v in self.nodes_list:
                        if u not in adj_list[v]:
                            adj_list[u].append([v, c])
                        else:
                            print(f"ERROR: No multiple edges")
                            return False
                    else:
                        print(f"ERROR: No such vertex {v}")
                        return False
                except KeyError:
                    print(f"ERROR: No such vertex {u}")
                    return False

        self.adj_list = adj_list
        return True

    def copy(self):
        pass

    def add_node(self, node):
        if node in self.nodes_list:
            print(f"ERROR: Unable to add vertex {node}. The same vertex already exist")
            return False
        self.adj_list[node] = []
        self.nodes_list.append(node)
        return True

    def add_edge(self, edge):
        v, u = edge[0], edge[1]
        c = '1'
        if self.weighted:
            try:
                c = edge[2]
            except KeyError:
                print(f"Unable to add the edge. No weight entered")
                return False
        try:
            if self.weighted:
                nodes = [x[0] for x in self.adj_list[v]]
                if u in nodes:
                    print(f"Do you want to change the weight of edge {v} {u} "
                          f"from {self.adj_list[v][nodes.index(u)][1]} to {c} "
                          f"Y/N")
                    ans = input()
                    if ans == "Y":
                        self.adj_list[v][nodes.index(u)][1] = c
            else:
                if [u, c] not in self.adj_list[v]:
                    self.adj_list[v].append([u, c])
                else:
                    print(f"Unable to add the edge. Same edge already exists")
                    return False

        except KeyError:
            print(f"Unable to add the edge. No such vertex {v}")
            return False

        if self.type != "directed":
            try:
                if self.weighted:
                    nodes = [x[0] for x in self.adj_list[u]]
                    if v in nodes:
                        print(f"Do you want to change the weight of edge {u} {v} "
                              f"from {self.adj_list[u][nodes.index(v)][1]} to {c} "
                              f"Y/N")
                        ans = input()
                        if ans == "Y":
                            self.adj_list[u][nodes.index(v)][1] = c
                else:
                    if [v, c] not in self.adj_list[u]:
                        self.adj_list[u].append([v, c])
                    else:
                        print(f"Unable to add the edge. Same edge already exists")
                        return False
            except KeyError:
                print(f"Unable to add the edge. No such vertex {u}")
                return False
        return True

    def delete_node(self, node):
        try:
            for item in self.adj_list.items():
                nodes = [x[0] for x in item[1]]
                if node in nodes:
                    del self.adj_list[item[0]][nodes.index(node)]
            del self.adj_list[node]
            del self.nodes_list[self.nodes_list.index(node)]
        except KeyError:
            print(f"ERROR: No such vertex {node}")
            return False
        return True

    def delete_edge(self, edge):
        v, u = edge[0], edge[1]

        try:
            nodes = [x[0] for x in self.adj_list[v]]
            del self.adj_list[v][nodes.index(u)]
        except (KeyError, ValueError):
            print(f"ERROR: No such edge ({v}, {u})")
            return False

        if self.type != "directed":
            try:
                nodes = [x[0] for x in self.adj_list[u]]
                del self.adj_list[u][nodes.index(v)]
            except (KeyError, ValueError):
                print(f"ERROR: No such edge ({u}, {v})")
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
        print("weighted" if self.weighted else "!weighted", file=fout)
        print(len(self.nodes_list), len(lst), file=fout)
        print(" ".join(self.nodes_list), file=fout)
        for edge in lst:
            print(f"{edge[0]} {edge[1]}", file=fout)
        return True

    def print_to_console(self):
        print(self.adj_list)
