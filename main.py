from graph import Graph

if __name__ == '__main__':
    gph = Graph()
    gph.print_to_console()
    print(gph.create_edge_list())
    gph.create_from_file("input.txt")
    gph.print_to_console()
    print(gph.create_edge_list())

