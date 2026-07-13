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
    
    def is_connected(self):

        if not self.graph:
            return True

        # armamos un grafo "no dirigido" temporal, ignorando las flechas
        undirected = {}

        for vertex in self.graph:
            undirected[vertex] = set()

        for source in self.graph:
            for target, weight in self.graph[source]:
                undirected[source].add(target)
                undirected[target].add(source)

        # recorrido tipo BFS desde un nodo cualquiera
        start = next(iter(self.graph))
        visited = set()
        queue = [start]

        while queue:
            current = queue.pop(0)

            if current not in visited:
                visited.add(current)

                for neighbor in undirected[current]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        # si visitamos todos los nodos, es conexo
        return len(visited) == len(self.graph)
    
    def is_dag(self):

        # para saber si es DAG (sin ciclos) vamos recorriendo el grafo
        # y nos fijamos si en el camino actual nos topamos con un nodo
        # que ya estabamos visitando ahorita mismo (no uno que ya terminamos)
        # si pasa eso, es porque hay un ciclo
        state = {vertex: 0 for vertex in self.graph}  # 0=nuevo, 1=lo estamos visitando, 2=ya lo terminamos

        def hay_ciclo(vertex):

            state[vertex] = 1

            for target, weight in self.graph[vertex]:

                if state[target] == 1:
                    return True

                if state[target] == 0 and hay_ciclo(target):
                    return True

            state[vertex] = 2
            return False

        for vertex in self.graph:

            if state[vertex] == 0:
                if hay_ciclo(vertex):
                    return False

        return True

    def _degrees(self):

        # esta funcion nos ayuda a contar cuantas flechas entran y cuantas
        # salen de cada nodo, la usamos para los dos puntos de Euler de abajo
        out_degree = {vertex: 0 for vertex in self.graph}
        in_degree = {vertex: 0 for vertex in self.graph}

        for source in self.graph:
            for target, weight in self.graph[source]:
                out_degree[source] += 1
                in_degree[target] += 1

        return in_degree, out_degree

    def has_euler_circuit(self):

        if not self.graph:
            return True

        # para que exista un circuito de Euler, a cada nodo le tienen que
        # entrar la misma cantidad de flechas que le salen, y ademas
        # el grafo tiene que ser conexo
        in_degree, out_degree = self._degrees()

        for vertex in self.graph:
            if in_degree[vertex] != out_degree[vertex]:
                return False

        return self.is_connected()

    def has_euler_path(self):

        if not self.graph:
            return True

        # para el camino de Euler es parecido al circuito, pero permitimos
        # que como mucho un nodo tenga una flecha de salida de mas (ahi
        # empezaria el camino) y como mucho un nodo tenga una de entrada
        # de mas (ahi terminaria), todos los demas deben quedar balanceados
        in_degree, out_degree = self._degrees()

        empiezan = 0
        terminan = 0

        for vertex in self.graph:

            diferencia = out_degree[vertex] - in_degree[vertex]

            if diferencia == 1:
                empiezan += 1
            elif diferencia == -1:
                terminan += 1
            elif diferencia != 0:
                return False

        if empiezan > 1 or terminan > 1:
            return False

        return self.is_connected()

    def dijkstra(self, source):

        # version clasica de Dijkstra, la mas facil de entender: en cada
        # vuelta buscamos el nodo no visitado mas cercano y actualizamos
        # las distancias de sus vecinos. ojo que esto solo funciona bien
        # si los pesos son positivos
        distances = {vertex: float("inf") for vertex in self.graph}

        if source not in distances:
            return distances

        distances[source] = 0
        visited = set()

        while len(visited) < len(self.graph):

            actual = None
            menor_distancia = float("inf")

            for vertex in self.graph:
                if vertex not in visited and distances[vertex] < menor_distancia:
                    actual = vertex
                    menor_distancia = distances[vertex]

            if actual is None:
                break

            visited.add(actual)

            for target, weight in self.graph[actual]:

                nueva_distancia = distances[actual] + weight

                if nueva_distancia < distances[target]:
                    distances[target] = nueva_distancia

        return distances