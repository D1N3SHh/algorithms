# binary search tree
# time complexity:  (h is the height of the tree)
#   search: O(h)
#   insert: O(h)
#   delete: O(h)
#   inorder_tree_walk: θ(n)
#   minimum: O(h)
#   maximum: O(h)

class Binary_search_tree():
    def __init__(self, root = None):
        self.root = root

    def __repr__(self):
        return str(self.root)

    def search(self, x, key):
        if x == None or key == x.data:
            return x
        if key < x.data:
            return self.search(x.left, key)
        else: return self.search(x.right, key)

    def insert(self, x):
        if self.root != None:
            parent = self.root
            while True:
                if x.data < parent.data:
                    if parent.left == None:
                        parent.left = x
                        break
                    else: parent = parent.left
                else:
                    if parent.right == None:
                        parent.right = x
                        break
                    else: parent = parent.right
            x.parent = parent
        else: self.root = x

    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else: u.parent.right = v
        if v != None: v.parent = u.parent

    def delete(self, x):
        if x.left == None:
            self.transplant(x, x.right)
        elif x.right == None:
            self.transplant(x, x.left)
        else:
            y = self.minimum(x.right)
            if y.parent != x:
                self.transplant(y, y.right)
                y.right = x.right
                y.right.parent = y
            self.transplant(x, y)
            y.left = x.left
            y.left.parent = y

    def inorder_tree_walk(self, x):
        if x != None:
            self.inorder_tree_walk(x.left)
            print(x.data, end=' ')
            self.inorder_tree_walk(x.right)

    def minimum(self, x):
        while x.left != None:
            x = x.left
        return x.data

    def maximum(self, x):
        while x.right != None:
            x = x.right
        return x.data


class Node():
    def __init__(self, data, parent = None, left = None, right = None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return '{%s:%s,%s}' % (self.data, self.left, self.right)


def example_usage():
    tree = Binary_search_tree()
    node_1 = Node(6)            #          6
    node_2 = Node(4)            #        /   \
    node_3 = Node(8)            #       4     8
    node_4 = Node(2)            #      /
    tree.insert(node_1)         #     2
    tree.insert(node_2)
    tree.insert(node_3)
    tree.insert(node_4)
    print('Tree text reprezentation:', tree)
    print('Searching for key = 4:', tree.search(tree.root, 4))
    print('Inorder walk:', end =' ')
    tree.inorder_tree_walk(tree.root)
    print('\nMinimum:', tree.minimum(tree.root))
    print('Maksimum:', tree.maximum(tree.root))
    tree.delete(node_2)
    print('Tree text reprezentation after removing node 2 (value=4):', tree)


if __name__ == "__main__":
    example_usage()