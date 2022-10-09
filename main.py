import graph
from graph import Graph

commands = {"CREATE EMPTY": "Create a new empty graph",
            "CREATE FROM FILE": "Create a new graph from the file",
            "CREATE A COPY": "Create the copy of existing graph",
            "ADD VERTEX": "Add a vertex to the graph",
            "ADD EDGE": "Add an edge to the graph",
            "DELETE VERTEX": "Remove a vertex from the graph",
            "DELETE EDGE": "Remove an edge from the graph",
            "PRINT LIST OF EDGES FILE": "Print list of edges to the file",
            "PRINT LIST OF EDGES CONSOLE": "Print list of edges to the console(there)",
            "PRINT ADJACENCY LIST TO CONSOLE": "Print adjacency list to the console(there)",
            "HELP": "Print the hint for the command",
            "EXIT": "Exit the execution",
            "PRINT LIST OF COMMANDS": "Print list of commands to the console(there)",
            "PRINT LIST OF GRAPHS": "Print list of graphs to the console(there)"}

graphs = {}


def print_menu():
    print("Enter the command from the list")
    for value in commands.keys():
        print(value)


def create(*filename):
    gr = Graph()
    fl = True
    if len(filename) == 1:
        fl = gr.create_from_file(filename[0])
    if fl:
        print("Enter the name for the new graph")
        name = input()
        while name in graphs.keys():
            print("This name already exists. Enter another")
            name = input()
        else:
            graphs[name] = gr


def get_graph_by_name():
    print("Enter the name of graph")
    name = input()
    while name not in graphs.keys():
        print("ERROR: NO SUCH GRAPH. Enter name again")
        name = input()
    return graphs[name]


if __name__ == '__main__':
    print_menu()
    print("\nENTER THE COMMAND: ", end="")
    command = input()
    while command != "EXIT":
        if command not in commands.keys():
            print("ERROR: UNKNOWN COMMAND")

        else:
            if command == "EXIT":
                exit(0)

            elif command == "HELP":
                fl = False
                print("To exit HELP enter STOP")
                print("Enter the name of command")
                name = input()
                while name != "STOP":
                    while name not in commands.keys():
                        if name == "STOP":
                            fl = True
                            break
                        print("Wrong value. Enter name of command again")
                        name = input()
                    else:
                        print(f"{name} : {commands[name]}")
                        print("To exit HELP enter STOP")
                    if fl:
                        break
                    print("Enter the name of command")
                    name = input()

            elif command == "CREATE EMPTY":
                create()
                pass

            elif command == "CREATE FROM FILE":
                print("Enter the name of file")
                create(input())
                pass

            elif command == "CREATE A COPY":
                pass

            elif command == "ADD VERTEX":
                cur_graph = get_graph_by_name()
                print("Enter the vertex to add: ", end="")
                node = input()
                cur_graph.add_node(node)

            elif command == "ADD EDGE":
                cur_graph = get_graph_by_name()
                print("Enter the edge to add in format "'begin end'": ", end="")
                edge = input().split()
                cur_graph.add_edge(edge)

            elif command == "DELETE VERTEX":
                cur_graph = get_graph_by_name()
                print("Enter the vertex to delete: ", end="")
                node = input()
                cur_graph.delete_node(node)

            elif command == "DELETE EDGE":
                cur_graph = get_graph_by_name()
                print('Enter the edge to delete in format "begin end":', end="")
                edge = input().split()
                cur_graph.delete_edge(edge)

            elif command == "PRINT LIST OF EDGES FILE":
                cur_graph = get_graph_by_name()
                print("Enter the name of file")
                filename = input()
                cur_graph.print_to_file(filename)

            elif command == "PRINT LIST OF EDGES CONSOLE":
                cur_graph = get_graph_by_name()
                print(cur_graph.create_edge_list())

            elif command == "PRINT ADJACENCY LIST TO CONSOLE":
                cur_graph = get_graph_by_name()
                cur_graph.print_to_console()

            elif command == "PRINT LIST OF COMMANDS":
                print_menu()

            elif command == "PRINT LIST OF GRAPHS":
                for gr in graphs.items():
                    print(f"Name: {gr[0]}\tAdjacency list: ", end="")
                    gr[1].print_to_console()

        print("\nENTER THE COMMAND: ", end="")
        command = input()
