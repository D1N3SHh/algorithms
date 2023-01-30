# linked list
# time complexity:
#   search: O(n)
#   insert: O(1)
#   delete: O(n)
# auxiliary space: O(n)


class Linked_list():
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "".join(str(nodes))

    def search(self, key):
        x = self.head
        while x != None and x.data != key:
            x = x.next
        return x

    def insert(self, x):
        x.next = self.head
        if self.head != None:
            self.head.prev = x
        self.head = x

    def delete(self, x):
        if x.prev != None:
            x.prev.next = x.next
        else: self.head = x.next
        if x.next != None:
            x.next.prev = x.prev


class Node():
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next


def  example_usage():
    linked_list = Linked_list()
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    linked_list.insert(node_1)
    linked_list.insert(node_2)
    linked_list.insert(node_3)
    linked_list.insert(node_4)
    print("List on start:", linked_list)
    print("Searching for key '3':", linked_list.search(3))
    linked_list.delete(node_3)
    print("List after removing 'node 3':", linked_list)


if __name__ == "__main__":
    example_usage()