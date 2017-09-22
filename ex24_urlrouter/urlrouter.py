from tstree import TSTree

class URLNode(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value


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
        key = lambda x: len(x.key)
        possibles = sorted(self.match_all(url), key=key)
        return possibles and possibles[0] or None

    def match_longest(self, url):
        key = lambda x: len(x.key)
        possibles = sorted(self.match_all(url), key=key)
        return possibles and possibles[-1] or None


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
        results = self.tree.find_all(url)
        return results


class DictRouter(URLRouter):

    def __init__(self):
        self.urls = {}

    def add(self, url, value):
        self.urls[url] = URLNode(url, value)

    def exact_match(self, url):
        node = self.urls.get(url)
        return node and node.value or None

    def best_match(self, url):
        possible = sorted(self.match_all(url))
        return possible and possible[0] or None
        
    def match_all(self, url):
        results = []
        for k,v in self.urls.items():
            if url.startswith(k):
                results.append(v)
        return results



