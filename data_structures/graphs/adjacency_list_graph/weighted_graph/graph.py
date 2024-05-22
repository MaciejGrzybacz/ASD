class WeightedGraph:
    def __init__(self):
        self.vertices = {}
        self.edges = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 in self.vertices:
            self.vertices[vertex1].append(vertex2)
        else:
            self.vertices[vertex1] = [vertex2]

        if (vertex1, vertex2) in self.edges or (vertex2, vertex1) in self.edges:
            # we do not support parallel edges
            self.edges[(vertex1, vertex2)] = weight
        else:
            self.edges[(vertex1, vertex2)] = weight

    def remove_edge(self, vertex1, vertex2):
        if (vertex1, vertex2) in self.edges:
            del self.edges[(vertex1, vertex2)]
        if vertex2 in self.vertices[vertex1]:
            self.vertices[vertex1].remove(vertex2)


    def remove_vertex(self, vertex):
        if vertex in self.vertices:
            del self.vertices[vertex]
        for v in self.vertices:
            if vertex in self.vertices[v]:
                self.vertices[v].remove(vertex)
                del self.edges[(v, vertex)]
        for v in self.vertices:
            if (vertex, v) in self.edges:
                del self.edges[(vertex, v)]

    def print_graph(self):
        for vertex in self.vertices:
            print(vertex, end=": ")
            for neighbor in self.vertices[vertex]:
                print(f"{neighbor}({self.edges[(vertex, neighbor)]})", end=" ")
            print()

    def get_vertices(self):
        return self.vertices

    def get_edges(self):
        return self.edges

    def get_neighbors(self, vertex):
        return self.vertices[vertex]

    def is_connected(self, vertex1, vertex2):
        return vertex2 in self.vertices[vertex1]

    def __str__(self):
        return str(self.vertices)

    def __repr__(self):
        return str(self.vertices)
