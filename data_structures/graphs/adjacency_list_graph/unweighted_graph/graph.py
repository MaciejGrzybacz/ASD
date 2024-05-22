class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices:
            self.vertices[vertex1].append(vertex2)
            self.edges.append((vertex1, vertex2))
        else:
            self.vertices[vertex1] = [vertex2]
            self.edges.append((vertex1, vertex2))

    def remove_vertex(self, vertex):
        if vertex in self.vertices:
            del self.vertices[vertex]
            for key in self.vertices:
                if vertex in self.vertices[key]:
                    self.vertices[key].remove(vertex)
            self.edges = [edge for edge in self.edges if vertex not in edge]

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices:
            if vertex2 in self.vertices[vertex1]:
                self.vertices[vertex1].remove(vertex2)
                self.edges = [edge for edge in self.edges if (vertex1, vertex2) != edge]

    def print_graph(self):
        for vertex in self.vertices:
            print(vertex, end=": ")
            for neighbor in self.vertices[vertex]:
                print(neighbor, end=" ")
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