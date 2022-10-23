import graph


def in_deg(graph, node):
    if node not in graph.nodes_list:
        print(f"No such vertex {node}")
        return -1
    ans = 0
    neib = []
    for item in graph.adj_list.items():
        nodes = [x[0] for x in item[1]]
        if node in nodes:
            neib.append(item[0])
            ans += 1
    return ans, neib


def new_graph(graph):
    gr = graph.copy()
    del_nodes = []
    for node in gr.adj_list.items():
        if len(node[1]) % 2 != 0:
            del_nodes.append(node[0])
    for node in del_nodes:
        gr.delete_node(node)
    return gr


def dfs(node):
    pass
