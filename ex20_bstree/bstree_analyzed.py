class BSTreeNode(object):

    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return f"{self.key}={self.value}:{self.left}:{self.right}:^{self.parent}"


class BSTree(object):
    
    def __init__(self):
        self.root = None

    def get(self, key, default=None):
        """Get the value for the tree."""
        # start at the root

        # if node.key = node.value
            # return node.value

        # if no left and right child:
            # return None
        # elif key < node key:
            # You go left if the given key is less-than the node's key.  
            # node = node.left
        # else:
            # You go right if the key is greater-than the node's key.
            # node = node.right

        # return None

    def set(self, key, value):
        """Sets the key to the value, replacing any existing value."""
        # start at the root

        # if node.key = node.value
            # set value to new value

        # if no left and right child:
            # add a new node to the left or right depending on equality
        # elif key < node key:
            # You go left if the given key is less-than the node's key.  
            # node = node.left
        # else:
            # You go right if the key is greater-than the node's key.
            # node = node.right

    def delete(self, key):
        """Deletes the given key from the data structure."""
        # The D node is a "leaf" node because it has no children (not left or right).
        # Just remove it from the parent.

        # The D node has only one child (either left or right but not both). In
        # that case you can simply move the value of this child to the D node,
        # then delete the child. That effectively replaces the D node with the
        # child (or, "moves the child up").

        # The D node has both a left and right child, which means it's time to do
        # some major surgery. First, find the minimum child of the D.right node
        # called the successor. Set the D.key to the successor.key, and then do
        # the same delete on this successor's children using its key.

    def list(self):
        """List the elements in the tree."""
        # start at the root
        # go left
        # when there is no left print value
        # go right
        # when there is no right print value



