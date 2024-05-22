import pytest
from .graph import Graph


def test_add_vertex():
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    assert graph.get_vertices() == {1: [], 2: [], 3: [], 4: []}


def test_add_edge():
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 4)
    assert graph.get_vertices() == {1: [2, 3, 4], 2: [3, 4], 3: [4], 4: []}
    assert graph.get_edges() == [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]


def test_remove_vertex():
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 4)
    graph.remove_vertex(1)
    assert graph.get_vertices() == {2: [3, 4], 3: [4], 4: []}
    assert graph.get_edges() == [(2, 3), (2, 4), (3, 4)]
    graph.remove_vertex(2)
    assert graph.get_vertices() == {3: [4], 4: []}
    assert graph.get_edges() == [(3, 4)]
    graph.remove_vertex(3)
    assert graph.get_vertices() == {4: []}
    assert graph.get_edges() == []
    graph.remove_vertex(4)
    assert graph.get_vertices() == {}
    assert graph.get_edges() == []


def test_remove_edge():
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 4)
    graph.remove_edge(1, 2)
    assert graph.get_vertices() == {1: [3, 4], 2: [3, 4], 3: [4], 4: []}
    assert graph.get_edges() == [(1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    graph.remove_edge(1, 3)
    assert graph.get_vertices() == {1: [4], 2: [3, 4], 3: [4], 4: []}
    assert graph.get_edges() == [(1, 4), (2, 3), (2, 4), (3, 4)]
    graph.remove_edge(1, 4)
    assert graph.get_vertices() == {1: [], 2: [3, 4], 3: [4], 4: []}
    assert graph.get_edges() == [(2, 3), (2, 4), (3, 4)]
    graph.remove_edge(2, 3)
    assert graph.get_vertices() == {1: [], 2: [4], 3: [4], 4: []}
    assert graph.get_edges() == [(2, 4), (3, 4)]
    graph.remove_edge(2, 4)
    assert graph.get_vertices() == {1: [], 2: [], 3: [4], 4: []}
    assert graph.get_edges() == [(3, 4)]
    graph.remove_edge(3, 4)
    assert graph.get_vertices() == {1: [], 2: [], 3: [], 4: []}
    assert graph.get_edges() == []


def test_print_graph(capsys):
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 4)
    graph.print_graph()
    captured = capsys.readouterr()
    assert captured.out == '1: 2 3 4 \n2: 3 4 \n3: 4 \n4: \n'


def test_get_neighbors():
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 4)
    assert graph.get_neighbors(1) == [2, 3, 4]
    assert graph.get_neighbors(2) == [3, 4]
    assert graph.get_neighbors(3) == [4]
    assert graph.get_neighbors(4) == []


def test_is_connected():
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 4)
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


def test_str():
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 4)
    assert str(graph) == '{1: [2, 3, 4], 2: [3, 4], 3: [4], 4: []}'
