import dllist
import bstree

def _search_list(data, elem, low, high):
    if low >= high:
        return None, -1
    else:
        mid = (high - low) // 2 + low
        mid_val = data[mid]

        if mid_val == elem:
            return elem, mid
        elif mid_val > elem:
            return _search_list(data, elem, low, mid)
        elif mid_val < elem:
            return _search_list(data, elem, mid + 1, high)

def search_list(data, elem):
    return _search_list(data, elem, 0, len(data))

def search_list_iter(data, elem):
    low = 0
    high = len(data)

    while low < high:
        mid = (high - low) // 2 + low
        mid_val = data[mid]

        if mid_val == elem:
            return elem, mid
        elif mid_val > elem:
            high = mid
        elif mid_val < elem:
            low = mid + 1

    return None, -1

def search_dllist(data, elem):
    dl = dllist.DoubleLinkedList()
    for x in data: dl.push(x)

    low = 0
    high = dl.count()

    while low < high:
        mid = (high - low) // 2 + low
        mid_val = dl.get(mid)

        if mid_val == elem:
            return elem, mid
        elif mid_val > elem:
            high = mid
        elif mid_val < elem:
            low = mid + 1

    return None, -1
    

def search_btree(data, elem):
    """Unlike the other functions this doesn't expect sorted data."""
    tree = bstree.BSTree()
    for i, key in enumerate(data):
        # use value for index
        tree.set(key, i)
  
    index = tree.get(elem)
    return index != None and (elem, index) or (None, -1)

