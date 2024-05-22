from .graph import WeightedGraph


def test_add_vertex():
    graph = WeightedGraph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    assert graph.get_vertices() == {1: [], 2: [], 3: [], 4: []}


def test_add_edge():
    graph = WeightedGraph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 2)
    graph.add_edge(1, 4, 3)
    graph.add_edge(2, 3, 4)
    graph.add_edge(2, 4, 5)
    graph.add_edge(3, 4, 6)
    assert graph.get_edges() == {(1, 2): 1, (1, 3): 2, (1, 4): 3, (2, 3): 4, (2, 4): 5, (3, 4): 6}


def test_print_graph(capsys):
    graph = WeightedGraph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 2)
    graph.add_edge(1, 4, 3)
    graph.add_edge(2, 3, 4)
    graph.add_edge(2, 4, 5)
    graph.add_edge(3, 4, 6)
    graph.print_graph()
    captured = capsys.readouterr()
    assert captured.out == '1: 2(1) 3(2) 4(3) \n2: 3(4) 4(5) \n3: 4(6) \n4: \n'

def test_remove_edge():
    graph = WeightedGraph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 2)
    graph.add_edge(1, 4, 3)
    graph.add_edge(2, 3, 4)
    graph.add_edge(2, 4, 5)
    graph.add_edge(3, 4, 6)
    graph.remove_edge(1, 2)
    graph.remove_edge(1, 3)
    graph.remove_edge(1, 4)
    graph.remove_edge(2, 3)
    graph.remove_edge(2, 4)
    graph.remove_edge(3, 4)
    assert graph.get_edges() == {}


def test_remove_vertex():
    graph = WeightedGraph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 2)
    graph.add_edge(1, 4, 3)
    graph.add_edge(2, 3, 4)
    graph.add_edge(2, 4, 5)
    graph.add_edge(3, 4, 6)
    graph.remove_vertex(1)
    graph.remove_vertex(2)
    graph.remove_vertex(3)
    graph.remove_vertex(4)
    assert graph.get_vertices() == {}
def test_get_neighbors():
    graph = WeightedGraph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 2)
    graph.add_edge(1, 4, 3)
    graph.add_edge(2, 3, 4)
    graph.add_edge(2, 4, 5)
    graph.add_edge(3, 4, 6)
    assert graph.get_neighbors(1) == [2, 3, 4]
    assert graph.get_neighbors(2) == [3, 4]
    assert graph.get_neighbors(3) == [4]
    assert graph.get_neighbors(4) == []


def test_is_connected():
    graph = WeightedGraph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 2)
    graph.add_edge(1, 4, 3)
    graph.add_edge(2, 3, 4)
    graph.add_edge(2, 4, 5)
    graph.add_edge(3, 4, 6)
    assert graph.is_connected(1, 2) == True
    assert graph.is_connected(1, 3) == True
    assert graph.is_connected(1, 4) == True
    assert graph.is_connected(2, 3) == True
    assert graph.is_connected(2, 4) == True
    assert graph.is_connected(3, 4) == True
    assert graph.is_connected(1, 1) == False
    assert graph.is_connected(2, 1) == False
    assert graph.is_connected(3, 1) == False
    assert graph.is_connected(4, 1) == False
    assert graph.is_connected(3, 2) == False
    assert graph.is_connected(4, 2) == False
    assert graph.is_connected(4, 3) == False
    assert graph.is_connected(1, 5) == False
