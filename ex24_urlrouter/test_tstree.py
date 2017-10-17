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

def test_TSTree_find_all():
    urls = test_TSTree_get_set()
    results = [n.value for n in urls.find_all("/k")]
    assert results == ["Kiwi", "Kumquat"]

def test_TSTree_find_shortest():
    urls = test_TSTree_get_set()
    urls.set("/kiwikiwi/", "KiwiKiwi")
    assert urls.find_shortest("/k").value == "Kiwi" 
    assert urls.find_shortest("/kiwiki").value == "KiwiKiwi"
    assert urls.find_shortest("/a").value == "Apple" 
    assert urls.find_shortest("/").value == "Kiwi" 


def test_TSTree_find_longest():
    urls = test_TSTree_get_set()
    assert urls.find_longest("/").value == "Pineapple" 


def test_TSTree_find_part():
    urls = test_TSTree_get_set()
    assert urls.find_part("/kaler").value == "Kiwi"
    assert urls.find_part("/application").value == "Apple"
    assert urls.find_part("/papal").value == "Pineapple"
    assert urls.find_part("/apple/120/1000/").value == "Apple"
    assert urls.find_part("/kiwi/user/zedshaw/has/stuff").value == "Kiwi"
    assert urls.find_part("XTREEME") == None


