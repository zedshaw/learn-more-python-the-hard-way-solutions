from dllist import DoubleLinkedList()

class Queue(object):

    def __init__(self):
        self.list = DoubleLinkedList()

    def shift(self, obj):
        """Shifts a new element onto the back of the queue."""
        self.list.shift()

    def unshift(self):
        """Removes the element that is first in the queue."""
        self.list.unshift()

