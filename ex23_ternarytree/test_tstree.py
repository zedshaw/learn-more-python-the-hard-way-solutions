from tstree import *


def test_get_set():
    urls = TSTree()
    urls.set("/books/", "Books")
    urls.set("/zed/", "Zed")
    urls.set("/frank/", "Frank")
    assert urls.get("/zed/") == "Zed"
    assert urls.get("/books/") == "Books"
    assert urls.get("/frank/") == "Frank"
    assert urls.get("/") == None

    return urls

