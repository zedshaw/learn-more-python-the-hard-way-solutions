from urlrouter import *


def test_TSTRouter_add():
    urls = TSTRouter()
    urls.add("/kiwi/", "Kiwi")
    urls.add("/apple/", "Apple")
    return urls

def test_TSTRouter_exact_match():
    urls = test_TSTRouter_add()
    assert urls.exact_match("/kiwi/") == "Kiwi"
    assert urls.exact_match("/apple/") == "Apple"
    assert urls.exact_match("/stuff/") == None

def test_TSTRouter_best_match():
    urls = test_TSTRouter_add()
    assert urls.best_match("/kiwi/user/1234/").value == "Kiwi"
    assert urls.best_match("/apple/user/2344/").value == "Apple"
    assert urls.best_match("NOTHING") == None

def test_TSTRouter_match_all():
    urls = test_TSTRouter_add()
    urls.add("/kiwikiwi/", "KiwiKiwi")
    all = [n.value for n in urls.match_all("/kiwi")]
    assert all == ["Kiwi", "KiwiKiwi"]

def test_TSTRouter_match_shortest():
    urls = test_TSTRouter_add()
    urls.add("/kiwikiwi/", "KiwiKiwi")
    assert urls.match_shortest("/k").value == "Kiwi"
    assert urls.match_shortest("/a").value == "Apple"

def test_TSTRouter_match_longest():
    urls = test_TSTRouter_add()
    urls.add("/kiwikiwi/", "KiwiKiwi")
    assert urls.match_longest("/k").value == "KiwiKiwi"
    assert urls.match_longest("/a").value == "Apple"


def test_DictRouter_add():
    urls = DictRouter()
    urls.add("/kiwi/", "Kiwi")
    urls.add("/apple/", "Apple")
    return urls

def test_DictRouter_exact_match():
    urls = test_DictRouter_add()
    assert urls.exact_match("/kiwi/") == "Kiwi"
    assert urls.exact_match("/apple/") == "Apple"
    assert urls.exact_match("/stuff/") == None

def test_DictRouter_best_match():
    urls = test_DictRouter_add()
    assert urls.best_match("/kiwi/user/1234/").value == "Kiwi"
    assert urls.best_match("/apple/user/2344/").value == "Apple"
    assert urls.best_match("NOTHING") == None

def test_DictRouter_match_all():
    urls = test_DictRouter_add()
    urls.add("/kiwikiwi/", "KiwiKiwi")
    all = [n.value for n in urls.match_all("/kiwi/")]
    assert all == ["Kiwi"]

def test_DictRouter_match_shortest():
    urls = test_DictRouter_add()
    urls.add("/k/", "KiwiKiwi")
    assert urls.match_shortest("/k/").value == "KiwiKiwi"

def test_DictRouter_match_longest():
    urls = test_DictRouter_add()
    urls.add("/kiwikiwi/", "KiwiKiwi")
    assert urls.match_longest("/kiwikiwi/").value == "KiwiKiwi"
    assert urls.match_longest("/apple/").value == "Apple"


