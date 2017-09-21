class TSTreeNode(object):
    
    def __init__(self, char, key, value, low, eq, high):
        self.char = char
        self.key = key
        self.low = low
        self.eq = eq
        self.high = high
        self.value = value

    def __repr__(self):
        return f"{self.key}:{self.value}<{self.low and self.low.key}={self.eq and self.eq.key}={self.high and self.high.key}>"

class TSTree(object):

    def __init__(self):
        self.root = None

    def _get(self, node, chars):
        char = chars[0]
        if node == None:
            return None
        elif char < node.char:
            return self._get(node.low, chars)
        elif char == node.char:
            if len(chars) > 1:
                return self._get(node.eq, chars[1:])
            else:
                return node
        else:
            return self._get(node.high, chars)

    def get(self, key):
        chars = [ord(x) for x in key]
        node = self._get(self.root, chars)
        return node and node.value or None

    def _set(self, node, chars, key, value):
        next_char = chars[0]

        if not node:
            # what happens if you add the value here?
            node = TSTreeNode(next_char, None, None, None, None, None)

        if next_char < node.char:
            node.low = self._set(node.low, chars, key, value)
        elif next_char == node.char:
            if len(chars) > 1:
                node.eq = self._set(node.eq, chars[1:], key, value)
            else:
                # what happens if you DO NOT add the value here?
                node.value = value
                node.key = key
        else:
            node.high = self._set(node.high, chars, key, value)

        return node

    def set(self, key, value):
        chars = [ord(x) for x in key]
        self.root = self._set(self.root, chars, key, value)

    def find_shortest(self, key):
        nodes = self.find_all(key)
        if nodes:
            shortest = nodes[0]
            for node in nodes:
                if len(node.key) < len(shortest.key):
                    shortest = node
            return shortest
        else:
            return None

    def find_longest(self, key):
        nodes = self.find_all(key)
        longest = nodes[0]
        for node in nodes:
            if len(node.key) > len(longest.key):
                longest = node
        return longest

    def _find_all(self, node, key, results):
        if not node: return

        if node.key and node.value:
            # this node has something so save it
            results.append(node)

        # if there is a low then go low
        if node.low:
            self._find_all(node.low, key, results)

        if node.eq:
        # now follow middle
            self._find_all(node.eq, key, results)

        if node.high:
        # if there is a high then go high
            self._find_all(node.high, key, results)


    def find_all(self, key):
        results = []
        chars = [ord(x) for x in key]
        start = self._get(self.root, chars)
        if start:
            self._find_all(start.eq, key, results)
        return results


    def find_part(self, key):
        """The difference between part and shortest is this:
        If you give find_part a 10 char key, and only 2 chars of the key
        match 2 chars in the TSTree, then it will return that key.  It is
        partial on *both* search key and key/value key.

        If you give a 10 char key to shortest, and only 2 chars match then
        it doesn't find anything.
        """
        # start by just finding the shortest key starting with the first char
        found = self.find_shortest(key[:1])
        if not found: return None

        # now if we found something then keep increasing the key
        for i in range(2, len(key)):
            stem = key[:i]
            node = self.find_shortest(stem)
            if not node:
                # didn't find something with the new key, so return what
                # we've found so far
                return found
            else:
                # found something, so update the best match so far
                found = node

        return found
