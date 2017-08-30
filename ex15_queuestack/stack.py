class StackNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"

class Stack(object):

    def __init__(self):
        self.top = None

    def push(self, obj):
        """Pushes a new value to the top of the stack."""
        self.top = StackNode(obj, self.top)

    def pop(self):
        """Pops the value that is currently on the top of the stack."""
        if self.top:
            node = self.top
            self.top = node.next
            return node.value
        else:
            return None

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        return self.top != None and self.top.value or None

    def count(self):
        """Counts the number of elements in the stack."""
        # same old count
        count = 0
        node = self.top
        while node:
            count += 1
            node = node.next
        return count

    def dump(self, mark="----"):
        """Debugging function that dumps the contents of the stack."""
        # same old dump
        print(">>>>> ", end="")
        node = self.top
        while node:
            print(node)
        print()

