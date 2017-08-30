import bsearch


def test_bsearch_list():
    data = sorted([5,3,7,1,9,20])
    assert bsearch.search_list(data, 5) == (5, 2)
    assert bsearch.search_list(data, 1) == (1, 0)
    assert bsearch.search_list(data, 20) == (20, len(data) - 1)
    assert bsearch.search_list(data, 9) == (9, 4)
    assert bsearch.search_list(data, 100) == (None, -1)
    assert bsearch.search_list(data, -1) == (None, -1)

def test_bsearch_list_iter():
    data = sorted([5,3,7,1,9,20])
    assert bsearch.search_list_iter(data, 5) == (5, 2)
    assert bsearch.search_list_iter(data, 1) == (1, 0)
    assert bsearch.search_list_iter(data, 20) == (20, len(data) - 1)
    assert bsearch.search_list_iter(data, 9) == (9, 4)
    assert bsearch.search_list_iter(data, 100) == (None, -1)
    assert bsearch.search_list_iter(data, -1) == (None, -1)

def test_bsearch_dllist():
    data = sorted([5,3,7,1,9,20])
    assert bsearch.search_dllist(data, 5) == (5, 2)
    assert bsearch.search_dllist(data, 1) == (1, 0)
    assert bsearch.search_dllist(data, 20) == (20, len(data) - 1)
    assert bsearch.search_dllist(data, 9) == (9, 4)
    assert bsearch.search_dllist(data, 100) == (None, -1)
    assert bsearch.search_dllist(data, -1) == (None, -1)

def test_btree_search():
    # for btree, adding sorted data just makes it a list
    data = [5,3,7,1,9,20]
    assert bsearch.search_btree(data, 5) == (5, 0)
    assert bsearch.search_btree(data, 1) == (1, 3)
    assert bsearch.search_btree(data, 20) == (20, len(data) - 1)
    assert bsearch.search_btree(data, 9) == (9, 4)
    assert bsearch.search_btree(data, 100) == (None, -1)
    assert bsearch.search_btree(data, -1) == (None, -1)


