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

print("\nIS CONNECTED?")
print(g.is_connected())

print("\nES DAG?")
print(g.is_dag())

print("\nTIENE CIRCUITO DE EULER?")
print(g.has_euler_circuit())

print("\nTIENE CAMINO DE EULER?")
print(g.has_euler_path())

print("\nDIJKSTRA DESDE EL VERTICE 0:")
print(g.dijkstra("0"))