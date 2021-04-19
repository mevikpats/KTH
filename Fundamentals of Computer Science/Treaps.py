# Oskar Mevik Päts, grudat21 up 2.5

import random

class _Node:
    def __init__(self,data):
        self._left = None
        self._right = None
        self._key = data
        self._prio = random.randint(0,2**64)

    def rotate_right(self):
        """Rotates the root to the right and returns the updated root."""
        child = self._left
        parent = self
        parent._left = child._right
        child._right = parent
        newnode = child
        return newnode

    def rotate_left(self):
        """Rotates the root to the left and returns the updated root."""
        child = self._right
        parent = self
        parent._right = child._left
        child._left = parent
        newnode = child
        return newnode


class BinaryTree: #Treap: Randomized search tree.
    """Create an empty treap."""
    def __init__(self):
        self._root = None
        self._size = 0

    # Worst case is O(log_2 n).
    def add(self,key):
        """Insert a new node in the tree and return the updated tree."""
        node = _Node(key)
        A = self._root
        self._size += 1
        self._root = self._add(node,self._root)

    def _add(self,node,root):
        if root is None:
            return node
        if node._key < root._key:
            root._left = self._add(node,root._left)

            if root._prio > root._left._prio:
                root = root.rotate_right()

        elif node._key > root._key:
            root._right = self._add(node,root._right)

            if root._prio > root._right._prio:
                root = root.rotate_left()

        elif node._key == root._key:
            self._size -= 1
        return root

    def size(self):
        """Returns the number of nodes in the treap."""
        return self._size

    def str(self):
        """Returns the nodes in alphabetical order in a list."""
        if self._root is None:
            return None
        else:
            list = []
            self._str(self._root,list)
            return list

    def _str(self,root,list):
        if root is not None:
            self._str(root._left,list)
            list.append(str(root._key))
            self._str(root._right,list)
        if root is None:
            return None
        return list

#Unit test.
def main():
    BT1 = BinaryTree()
    assert BT1.size() == 0
    BT1.add('Tango')
    assert BT1.size() == 1
    BT1.add('Echo')
    BT1.add('Tango')
    assert BT1.size() == 2
    BT1.add('Yankee')
    assert BT1.size() == 3
    BT1.add('Alfa')
    assert BT1.size() == 4
    BT1.add('Sierra')
    assert BT1.size() == 5
    exp = ['Alfa', 'Echo', 'Sierra', 'Tango', 'Yankee']
    assert BT1.str() == exp

if __name__ == "__main__":
    main()
