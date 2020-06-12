"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right == None: # value is greater than or equal to the node currently referred to as self and there is not another node that fits that description.
                self.right = BSTNode(value)
            else:
                self.right.insert(value) # rerun this method with the correct child node
        else:
            if self.left == None: # value is less than the node currently referred to as self and there is not another node that fits that description.
                self.left = BSTNode(value)
            else:
                self.left.insert(value) # rerun this method with the correct child node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target > self.value:
            if self.right == None:
                return False
            else:
                return self.right.contains(target)
        elif target < self.value:
            if self.left == None:
                return False
            else:
                return self.left.contains(target)
        else:
            return True

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        # start at root and run this method on each of the node's children (if any)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left: # if the current node has a left child node, run the method with that node as the argument
            node.in_order_print(node.left)
        print(node.value) # print the current node
        if node.right: # run this method with the right child of the current node if it exists
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = [node]

        while len(queue) > 0:
            current = queue.pop(0) # remove the current node from the list
            # add children to end of queue from left to right
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            print(current.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = [node] # initialize stack
        while len(stack) > 0:
            current = stack.pop()
            print(current.value)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Pre-order means you run the current node before either child
    # In-order means you run the left child, then the current node, and then the right child
    # Post-order node means you run both the left and the right children before running the current node

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            node.pre_order_dft(node.left)
        if node.right:
            node.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            node.post_order_dft(node.left)
        if node.right:
            node.post_order_dft(node.right)
        print(node.value)
