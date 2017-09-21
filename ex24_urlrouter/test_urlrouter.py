from urlrouter import TSTRouter


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
    pass

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


