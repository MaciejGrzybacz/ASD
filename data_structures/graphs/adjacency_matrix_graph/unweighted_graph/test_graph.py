from .graph import Graph

def test_add_undirected_edge():
    graph = Graph(5)
    graph.add_edge(0, 1, 1)
    graph.add_edge(0, 2, 2)
    graph.add_edge(0, 3, 3)
    graph.add_edge(1, 2, 4)
    graph.add_edge(1, 3, 5)
    graph.add_edge(2, 3, 6)
    graph.add_edge(3, 4, 7)

    assert graph.adj_matrix == [[0, 1, 2, 3, 0],
                                [1, 0, 4, 5, 0],
                                [2, 4, 0, 6, 0],
                                [3, 5, 6, 0, 7],
                                [0, 0, 0, 7, 0]]

def test_add_directed_edge():
    graph = Graph(5, directed=True)
    graph.add_edge(0, 1, 1)
    graph.add_edge(0, 2, 2)
    graph.add_edge(0, 3, 3)
    graph.add_edge(1, 2, 4)
    graph.add_edge(1, 3, 5)
    graph.add_edge(2, 3, 6)
    graph.add_edge(3, 4, 7)

    assert graph.adj_matrix == [[0, 1, 2, 3, 0],
                                [0, 0, 4, 5, 0],
                                [0, 0, 0, 6, 0],
                                [0, 0, 0, 0, 7],
                                [0, 0, 0, 0, 0]]


def test_remove_undirected_edge():
    graph = Graph(5)
    graph.add_edge(0, 1, 1)
    graph.add_edge(0, 2, 2)
    graph.add_edge(0, 3, 3)
    graph.add_edge(1, 2, 4)
    graph.add_edge(1, 3, 5)
    graph.add_edge(2, 3, 6)
    graph.add_edge(3, 4, 7)

    graph.remove_edge(0, 1)
    graph.remove_edge(0, 2)
    graph.remove_edge(0, 3)
    graph.remove_edge(1, 2)
    graph.remove_edge(1, 3)
    graph.remove_edge(2, 3)
    graph.remove_edge(3, 4)

    assert graph.adj_matrix == [[0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0]]

def test_remove_directed_edge():
    graph=Graph(5,directed=True)
    graph.add_edge(0, 1, 1)
    graph.add_edge(0, 2, 2)
    graph.add_edge(0, 3, 3)
    graph.add_edge(1, 2, 4)
    graph.add_edge(1, 3, 5)
    graph.add_edge(2, 3, 6)
    graph.add_edge(3, 4, 7)

    graph.remove_edge(0, 1)
    graph.remove_edge(0, 2)
    graph.remove_edge(0, 3)
    graph.remove_edge(1, 2)
    graph.remove_edge(1, 3)
    graph.remove_edge(2, 3)
    graph.remove_edge(3, 4)

    assert graph.adj_matrix == [[0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0]]
