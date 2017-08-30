from time import sleep

class QueueNode(object):

    def __init__(self, value, nxt, prv):
        self.value = value
        self.next = nxt
        self.prev = prv

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f"[{self.value}:next={repr(nval)}:prev={repr(pval)}]"


class Queue(object):

    def __init__(self):
        self.tail = None
        self.head = None

    def shift(self, obj):
        """Shifts a new element onto the back of the queue."""
        if self.tail:
            node = QueueNode(obj, None, self.tail)
            self.tail.next = node
            self.tail = node
        else:
            self.head = QueueNode(obj, None, None)
            self.tail = self.head

    def unshift(self):
        """Removes the element that is first in the queue."""
        if self.head:
            node = self.head

            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = node.next
                self.head.prev = None

            return node.value

        else:
            return None

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        return self.head and self.head.value or None

    def empty(self):
        """Indicates if the Queue is empty."""
        return self.head == None

    def count(self):
        """Counts the number of elements in the queue."""
        node = self.head
        i = 0
        while node:
            i += 1
            node = node.next

        return i

    def dump(self, mark='----'):
        """Debugging function that dumps the contents of the queue."""
        print(mark)
        node = self.head
        while node:
            print(node, " ", end='')
            node = node.next
        print()


