class DoubleLinkedListNode(object):

    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f"[{self.value}, {repr(nval)}, {repr(pval)}]"

class DoubleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        """Appends a new value on the end of the list."""
        # if there are contents
        if self.end:
            # new node with prev=end
            node = DoubleLinkedListNode(obj, None, self.end)
            # end.next = new node
            self.end.next = node
            # new end is node
            self.end = node
        # else begin and end are new node with none
        else:
            self.begin = DoubleLinkedListNode(obj, None, None)
            self.end = self.begin

    def pop(self):
        """Removes the last item and returns it."""
        # if we have some
        if self.end:
            # get the end node
            node = self.end
            # if there is one
            if self.end == self.begin:
                self.end = None
                self.begin = None
            else:
                # detach end and reset it
                # end = end.prev
                self.end = node.prev
                # end.next = None
                self.end.next = None
                # if there's now one left, set begin to end
                if self.end == self.begin:
                    self.begin.next = None
            return node.value
        else:
            return None

    def shift(self, obj):
        """Actually just another name for push."""
        self.push(obj)

    def unshift(self):
        """Removes the first item (from begin) and returns it."""
        # if we have one at begin
        if self.begin:
            # save the begin
            node = self.begin
            # if we have only one
            if self.begin == self.end:
                # clear begin and end
                self.begin = None
                self.end = None
            else:
                # set begin to begin.next
                self.begin = node.next
                # set begin.prev to None
                self.begin.prev = None
            return node.value
        else:
            return None

    def detach_node(self, node):
        """You'll need to use this operation sometimes, but mostly 
        inside remove().  It should take a node, and detach it from
        the list, whether the node is at the front, end, or in the middle."""
        if self.end == node:
            self.pop()
        elif self.begin == node:
            self.unshift()
        else:
            # skip over it
            # save node.prev, node.next
            nxt = node.next
            prev = node.next
            # set prev.next to saved next
            prev.next = nxt
            # set next.prev to saved prev
            next.prev = prev

    def remove(self, obj):
        """Finds a matching item and removes it from the list."""
        # start at the begin
        node = self.begin
        # keep the count as return value
        count = 0
        # while we have a node
        while node:
            # if the node.value matches obj
            if node.value == obj:
                self.detach_node(node)
                return count
            else:
                count += 1
                node = node.next
        # return -1 to indicate not there
        return -1

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        # if there's a begin return the value or None
        return self.begin and self.begin.value or None

    def last(self):
        """Returns a reference to the last item, does not remove."""
        # if there's an end return the value or None
        return self.end and self.end.value or None

    def count(self):
        """Counts the number of elements in the list."""
        # do the slow count code from single linked lists
        node = self.begin
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    def get(self, index):
        """Get the value at index."""
        # similar code to count, but stop at index and return value or None
        node = self.begin
        i = 0
        while node:
            if i == index:
                return node.value
            else:
                i += 1
                node = node.next
        return None


    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""
        # set node to begin
        node = self.begin
        print(mark, end="")
        # while there's a node, print it out
        while node:
            print(node, end="")
            node = node.next
        # print new line
        print()

    def _invariant(self):
        if self.begin == None:
            assert self.end == None, "End set while begin is not."

        if self.begin:
            assert self.begin.prev == None, "begin.prev not None"
            assert self.end.next == None, "end.next not None"

