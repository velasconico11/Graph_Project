class Graph:

    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):

        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, source, target, weight):

        self.add_vertex(source)
        self.add_vertex(target)

        self.graph[source].append((target, weight))

    def show_graph(self):

        for vertex in self.graph:
            print(vertex, "->", self.graph[vertex])

    def load_from_file(self, file_path):

        file = open(file_path, "r")

        next(file)

        for line in file:

            source, target, weight = line.strip().split(",")

            self.add_edge(source, target, int(weight))

        file.close()

    def vertex_degree(self, vertex):

        if vertex in self.graph:
            return len(self.graph[vertex])

        return 0

    def is_multigraph(self):

        edges = set()

        for source in self.graph:

            for target, weight in self.graph[source]:

                if source == target:
                    return True

                edge = (source, target)

                if edge in edges:
                    return True

                edges.add(edge)

        return False

    def is_complete(self):

        total_vertices = len(self.graph)

        for vertex in self.graph:

            if len(self.graph[vertex]) != total_vertices - 1:
                return False

        return True