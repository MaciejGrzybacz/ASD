# matrix implementation of unweighted graph

class Graph:
    def __init__(self, num_vertex, directed=False):
        self.adj_matrix = [[0] * num_vertex for _ in range(num_vertex)]
        self.num_vertex = num_vertex
        self.directed = directed

    def add_edge(self, v1, v2, weight):
        if v1 >= self.num_vertex or v2 >= self.num_vertex or v1 < 0 or v2 < 0:
            raise IndexError('Vertex out of bound')
        self.adj_matrix[v1][v2] = weight
        if not self.directed:
            self.adj_matrix[v2][v1] = weight

    def remove_edge(self, v1, v2):
        if v1 >= self.num_vertex or v2 >= self.num_vertex or v1 < 0 or v2 < 0:
            raise IndexError('Vertex out of bound')
        self.adj_matrix[v1][v2] = 0
        if not self.directed:
            self.adj_matrix[v2][v1] = 0

    def contains_edge(self, v1, v2):
        if v1 >= self.num_vertex or v2 >= self.num_vertex or v1 < 0 or v2 < 0:
            raise IndexError('Vertex out of bound')
        return self.adj_matrix[v1][v2] != 0


