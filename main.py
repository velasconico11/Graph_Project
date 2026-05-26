from graph import Graph

g = Graph()

g.load_from_file("grafo32.csv")

print("\nGRAPH:\n")

g.show_graph()

print("\nDEGREE OF VERTEX 0:")
print(g.vertex_degree("0"))

print("\nIS MULTIGRAPH?")
print(g.is_multigraph())

print("\nIS COMPLETE?")
print(g.is_complete())