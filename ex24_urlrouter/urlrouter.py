from tstree import TSTree
from dllist import DoubleLinkedList
from bstree import BSTree

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
        key = lambda x: len(x.key)
        possible = sorted(self.match_all(url), key=key)
        return possible and possible[0] or None

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
        self.urls = TSTree()

    def add(self, url, value):
        self.urls.set(url, value)

    def exact_match(self, url):
        return self.urls.get(url)

    def best_match(self, url):
        return self.urls.find_part(url)

    def match_all(self, url):
        results = self.urls.find_all(url)
        return results


class DictRouter(URLRouter):

    def __init__(self):
        self.urls = {}

    def add(self, url, value):
        self.urls[url] = URLNode(url, value)

    def exact_match(self, url):
        node = self.urls.get(url)
        return node and node.value or None

    def match_all(self, url):
        results = []
        for k,v in self.urls.items():
            if len(k) > len(url):
                if k.startswith(url):
                    results.append(v)
            else:
                if url.startswith(k):
                    results.append(v)

        return results

class BSTreeRouter(URLRouter):

    def __init__(self):
        self.urls = BSTree()

    def add(self, url, value):
        self.urls.set(url, URLNode(url, value))

    def exact_match(self, url):
        node = self.urls.get(url)
        return node and node.value or None

    def _match_all(self, results, node, url):
        if node:
            if len(node.key) > len(url):
                if node.key.startswith(url):
                    results.append(node.value)
            else:
                if url.startswith(node.key):
                    results.append(node.value)
            if node.left:
                self._match_all(results, node.left, url)
            if node.right:
                self._match_all(results, node.right, url)

        
    def match_all(self, url):
        results = []
        self._match_all(results, self.urls.root, url)
        return results


class DListRouter(URLRouter):

    def __init__(self):
        self.urls = DoubleLinkedList()

    def add(self, url, value):
        self.urls.push(URLNode(url, value))

    def exact_match(self, url):
        node = self.urls.begin

        while node:
            route = node.value
            if route.key == url:
                return route.value
            else:
                node = node.next

        return None

    def match_all(self, url):
        node = self.urls.begin
        results = []

        while node:
            route = node.value
            if len(route.key) > len(url):
                if route.key.startswith(url):
                    results.append(route)
            else:
                if url.startswith(route.key):
                    results.append(route)

            node = node.next

        return results
