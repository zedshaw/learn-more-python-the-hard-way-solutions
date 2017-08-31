class TSTreeNode(object):
    
    def __init__(self, key, value, low, eq, high):
        self.key = key
        self.low = low
        self.eq = eq
        self.high = high
        self.value = value


class TSTree(object):

    def __init__(self):
        self.root = None

    def _get(self, node, keys):
        key = keys[0]
        if key < node.key:
            return self._get(node.low, keys)
        elif key == node.key:
            if len(keys) > 1:
                return self._get(node.eq, keys[1:])
            else:
                return node.value
        else:
            return self._get(node.high, keys)

    def get(self, key):
        keys = [x for x in key]
        return self._get(self.root, keys)

    def _set(self, node, keys, value):
        next_key = keys[0]

        if not node:
            # what happens if you add the value here?
            node = TSTreeNode(next_key, None, None, None, None)

        if next_key < node.key:
            node.low = self._set(node.low, keys, value)
        elif next_key == node.key:
            if len(keys) > 1:
                node.eq = self._set(node.eq, keys[1:], value)
            else:
                # what happens if you DO NOT add the value here?
                node.value = value
        else:
            node.high = self._set(node.high, keys, value)

        return node

    def set(self, key, value):
        keys = [x for x in key]
        self.root = self._set(self.root, keys, value)

    def find_shortest(self, key):
        pass

    def find_longest(self, key):
        pass

    def find_all(self, key):
        pass

    def find_part(self, key):
        pass


