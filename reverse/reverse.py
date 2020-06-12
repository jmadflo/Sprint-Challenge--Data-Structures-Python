class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        stack = []
        last_node = None
        while node:
            stack.append(node.value)
            node = node.next_node
        # print(stack)
        while len(stack) > 0:
            last_val = stack.pop()
            # print(last_val)
            if last_node:
                last_node.next_node = Node(last_val)
                last_node = last_node.next_node
            else:
                self.head = Node(last_val)
                last_node = self.head
        # Failed attempt at recursion
        # new = LinkedList()
        # stack = []
        # if node.next_node:
        #     stack.append(node.value)
        #     node = self.reverse_list(node.next_node, node)
        #     value = stack.pop()
        #     node.next_node = Node(value)
        # else:
        #     new_linked_list = new.add_to_head(node.value)
        # return node 