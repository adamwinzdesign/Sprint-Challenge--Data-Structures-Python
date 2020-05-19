class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        node = self
        def find_node(node):
            if value < node.value:
                if node.left is None:
                    node.left = BSTNode(value)
                    # if value has been assigned, end recursion
                    return True
                else:
                    return find_node(node.left)
            else:
                if node.right is None:
                    node.right = BSTNode(value)
                    return True
                else:
                    return find_node(node.right)
        return find_node(node)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # compare target to self, which is the root
        # Return false when we know we need to go right or left based on comparison to the node, but that node does not have a corresponding child on that side.  Ex if target is 5, current node is 4 but it does not have a self.right
        if target == self.value:
            return True
        if target < self.value:
            # go left if possible and restart comparison, otherwise return false
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            # target must be greater than self because function would have already returned True if equal or False if less than
            # go right if possible and restart comparision, otherwise return false
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # if there is no self.right, return the current value
        # if there is a self.right, go to that node and check again until there is no self.right, then return the current value as above.
        while self.right is not None:
            self = self.right
        return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the fn on the value at this node 
        fn(self.value)

        # pass this function to the left child 
        if self.left:
            self.left.for_each(fn)
        # pass this function to the right child 
        if self.right:
            self.right.for_each(fn)