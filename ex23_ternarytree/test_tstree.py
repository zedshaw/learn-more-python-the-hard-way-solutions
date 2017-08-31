from tstree import *


def test_TSTree_get_set():
    urls = TSTree()
    urls.set("/apple/", "Apple")
    urls.set("/grape/", "Grape")
    urls.set("/kiwi/", "Kiwi")
    urls.set("/kumquat/", "Kumquat")
    urls.set("/pineapple/", "Pineapple")

    assert urls.get("/apple/") == "Apple"
    assert urls.get("/grape/") == "Grape"
    assert urls.get("/kiwi/") == "Kiwi"
    assert urls.get("/") == None

    return urls

def test_TSTree_find_shortest():
    urls = test_TSTree_get_set()
    assert urls.find_shortest("/") == "/kiwi/" 


def test_TSTree_find_longest():
    urls = test_TSTree_get_set()
    assert urls.find_longest("/") == "/pineapple/" 


def test_TSTree_find_all():
    urls = test_TSTree_get_set()
    assert urls.find_all("/k") == ["/kiwi/", "/kumquat/"]

def test_TSTree_find_part():
    urls = test_TSTree_get_set()
    assert urls.find_part("/") == []


