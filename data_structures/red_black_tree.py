# binary search tree
# author: D1N3SHh
# https://github.com/D1N3SHh/algorithms


class Red_black_tree():
    def __init__(self):
        self.nil = Node(0, 'black', None, None)
        self.root = self.nil
 

    def __repr__(self):
        return str(self.root)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else: x.parent.right = y
        x.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else: x.parent.left = y
        x.right = x
        x.parent = y

    def insert(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else: x = x.right
        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key or y.key == None:
            y.left = z
        else: y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = 'red'
        self.insert_fixup(z)

    def insert_fixup(self, z):
        while z != self.root and z.parent.color == 'red':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = 'black'                
                    z.parent.parent.color = 'red'
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.left_rotate(z.parent.parent)
        self.root.color = 'black'

    def transplant(self, u, v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else: u.parent.right = v
        v.parent = u.parent

    def delete(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 'black':
            self.delete_fixup(x)

    def delete_fixup(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'black':
                        w.left.color = 'black'
                        w.color = 'red'
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == 'black' and w.left.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.left.color == 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.left.color = 'black'
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 'black'

    def minimum(self, x):
        while x.left.left != None:
            x = x.left
        return x.key

    def maximum(self, x):
        while x.right.right != None:
            x = x.right
        return x.key 

    def search(self, x, key):
        if x == None or key == x.key:
            return x
        if key < x.key:
            return self.search(x.left, key)
        else: return self.search(x.right, key)


class Node():
    def __init__(self, key, color = 'red', parent = None, left = None, right = None):
        self.key = key
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return '{|%s%s|:%s,%s}' % (self.color, self.key, self.left, self.right)


def example_usage():
    rb_tree = Red_black_tree()
    node_1 = Node(6)            #          6
    node_2 = Node(4)            #        /   \
    node_3 = Node(8)            #       4     8
    node_4 = Node(2)            #      /
    rb_tree.insert(node_1)      #     2
    rb_tree.insert(node_2)
    rb_tree.insert(node_3)
    rb_tree.insert(node_4)
    print('Tree text reprezentation:', rb_tree)
    print('Searching for key = 4:', rb_tree.search(rb_tree.root, 4))
    print('Minimum:', rb_tree.minimum(rb_tree.root))
    print('Maksimum:', rb_tree.maximum(rb_tree.root))
    rb_tree.delete(node_2)
    print('Tree text reprezentation after removing node 2 (key=4):', rb_tree)

    
if __name__ == "__main__":
    example_usage() # run an example on start