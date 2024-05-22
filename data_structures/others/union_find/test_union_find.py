import pytest
from data_structures.others.union_find.union_find import UnionFind

def test_initialize_with_list():
    data = [1, 2, 3, 4, 5]
    uf = UnionFind(data)
    assert uf.data == data
    assert uf.comp_sizes == [1, 1, 1, 1, 1]
    assert uf.ids == [0, 1, 2, 3, 4]
    assert uf.comp_count == 5

def test_find_root():
    data = [1, 2, 3, 4, 5]
    uf = UnionFind(data)
    assert uf.find(0) == 0
    assert uf.find(1) == 1
    assert uf.find(2) == 2
    assert uf.find(3) == 3
    assert uf.find(4) == 4

def test_unify_components():
    data = [0, 1, 2, 3, 4]
    uf = UnionFind(data)
    uf.unify(0, 1)
    assert uf.ids == [1, 1, 2, 3, 4]
    assert uf.comp_sizes == [0, 2, 1, 1, 1]
    assert uf.comp_count == 4

def test_update_component_sizes_and_count():
    data = [0, 1, 2, 3, 4]
    uf = UnionFind(data)
    uf.unify(0, 1)
    uf.unify(2, 3)
    uf.unify(0, 2)
    assert uf.comp_sizes == [0, 0, 0, 4, 1]
    assert uf.comp_count == 2

def test_update_ids_list_after_unification():
    data = [0, 1, 2, 3, 4]
    uf = UnionFind(data)
    uf.unify(0, 1)
    uf.unify(2, 3)
    uf.unify(0, 2)
    assert uf.ids == [1, 3, 3, 3, 4]

def test_handle_empty_list_input():
    data = []
    uf = UnionFind(data)
    assert uf.data == []
    assert uf.comp_sizes == []
    assert uf.ids == []
    assert uf.comp_count == 0

def test_handle_single_element_input():
    data = [1]
    uf = UnionFind(data)
    assert uf.data == [1]
    assert uf.comp_sizes == [1]
    assert uf.ids == [0]
    assert uf.comp_count == 1

def test_handle_unify_different_components():
    data = [0, 1, 2, 3, 4]
    uf = UnionFind(data)
    uf.unify(0, 1)
    uf.unify(3, 4)
    uf.unify(0, 3)
    assert uf.ids == [1, 4, 2, 4, 4]

def test_find_root_in_component_of_size_1():
    data = [0, 1, 2, 3, 4]
    uf = UnionFind(data)
    assert uf.find(0) == 0
    assert uf.find(1) == 1
    assert uf.find(2) == 2
    assert uf.find(3) == 3
    assert uf.find(4) == 4

def test_handle_unify_components_of_equal_size():
    data = [0, 1, 2, 3, 4]
    uf = UnionFind(data)
    uf.unify(0, 1)
    uf.unify(2, 3)
    uf.unify(4, 0)
    assert uf.ids == [1, 1, 3, 3, 1]

def test_handle_unify_all_elements():
    data = [0, 1, 2, 3, 4]
    uf = UnionFind(data)
    uf.unify(0, 1)
    uf.unify(2, 3)
    uf.unify(4, 0)
    uf.unify(1, 2)
    uf.unify(3, 4)
    assert uf.ids == [1, 1, 3, 1, 1]
