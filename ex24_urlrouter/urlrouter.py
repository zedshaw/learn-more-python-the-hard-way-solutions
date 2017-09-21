from tstree import TSTree

class URLRouter(object):

    def __init__(self):
        pass

    def add(self, url, value):
        pass

    def exact_match(self, url):
        pass

    def best_match(self, url):
        pass

    def match_all(self, url):
        pass

    def match_shortest(self, url):
        pass

    def match_longest(self, url):
        pass


class TSTRouter(URLRouter):

    def __init__(self):
        self.tree = TSTree()

    def add(self, url, value):
        self.tree.set(url, value)

    def exact_match(self, url):
        return self.tree.get(url)

    def best_match(self, url):
        return self.tree.find_part(url)

    def match_all(self, url):
        pass

    def match_shortest(self, url):
        return self.tree.find_shortest(url)

    def match_longest(self, url):
        return self.tree.find_longest(url)

