# Oskar Mevik Päts, grudat21 uppg 1.2

class _listElement:
    def __init__(self, _data, _next = None):
        self._data = _data
        self._next = _next


class linkedList: # A singly linked list of elements of type T.
    """Create an empty list."""

    def __init__(self):
        self._first = None  # first element in list
        self._last = None   # last element in list
        self._size = 0   # number of elements in list

    def addFirst(self, _n):
        """Insert the given element at the beginning of this list."""

        _FE = _listElement(_n)
        self._size += 1
        if self._first is None:
            self._first = _FE
            self._last = _FE
        else:
            _FE._next = self._first
            self._first = _FE


    def addLast(self, k):
        """Insert the given element at the end of this list."""

        _LE = _listElement(k)
        self._size += 1
        if self._first is None:
            self._first = _LE
            self._last = _LE
        else:
            self._last._next = _LE
            self._last = _LE

    def getFirst(self):
        """Return the first element of this list.

        Return None if the list is empty.
        """

        if self._first is None:
            return None
        return self._first._data

    def getLast(self):
        """Return the last element of this list.

        Return None if the list is empty.
        """

        if self._last is None:
            return None
        return self._last._data

    def getIndex(self,index):
        """Return the element at the specified position in this list.

        Return None if index is out of bounds."""

        if self._first is None:
            return None
        _counter = 0
        _n = self._first
        while _counter != index:
            _n = _n._next
            _counter += 1
            if _n is None:
                return None
        return _n._data

    def removeFirst(self):
        """Remove and returns the first element from this list.

        Return None if the list is empty."""

        if self._first is None:
            return None
        first_element = self._first._data
        if self._size == 1:
            self._first = None
            self._last = None
        self._first = self._first._next
        self._size += -1
        return first_element

    def clear(self):
        """Remove all elements from this list."""

        self._first = None
        self._last = None
        self._size = 0

    def size(self):
        """Return the number of elements in this list."""

        return self._size

    def string(self):
        """Return a string representation of this list.

        The elements are enclosed in square brackets ("[]").

        Adjacent elements are separated by ", ".
        """

        string = ""
        _n = self._first
        if _n is None:
            return string
        while _n is not None:
            string += str([_n._data]) + ','
            _n = _n._next
        return string[:-1]


def new():
    return linkedList()


# unit test

def main():
    LL = new()
    empty = new()
    assert LL._size == 0
    assert LL._first == LL._last == None
    assert healthy(LL)

    LL.addFirst('Alpha')
    assert LL._first._data == 'Alpha'
    LL.addFirst(999)
    assert LL._first._data == 999
    assert LL._first._next._data == 'Alpha'
    assert healthy(LL)

    LL.addLast('Beta')
    assert LL._first._data == 999
    assert LL._first._next._data == 'Alpha'
    assert LL._first._next._next._data == 'Beta'
    assert healthy(LL)


    assert empty.getFirst() == None
    assert LL.getFirst() == 999

    assert empty.getLast() == None
    assert LL.getLast() == 'Beta'

    assert empty.getIndex(0) == None
    assert empty.getIndex(23) == None
    assert LL.getIndex(1) == 'Alpha'
    assert LL.getIndex(3) == None

    assert empty.removeFirst() == None
    assert LL.removeFirst() == 999
    assert LL.getFirst() == 'Alpha'
    assert healthy(LL)
    assert healthy(empty)

    LL.clear()
    empty.clear()

    assert LL._first == LL._last == None
    assert empty._first == empty._last == None
    assert empty._size == LL._size == 0
    assert healthy(LL)
    assert healthy(empty)

    LL.addFirst(1.0)
    LL.addLast('Two')
    LL.addLast(3)


    assert LL.size() == 3
    assert empty.size() == 0
    assert healthy(LL)

    exp = "[1.0],['Two'],[3]"
    assert LL.string() == exp
    assert empty.string() == ''
    assert healthy(LL)

def healthy(list):
    """Checks if the list is still compact. Returns true if size is the number of elements and _last._next is None,
    and if the list is empty then makes sure that _first = _last = None.

    """

    A = False
    B = False

    counter = 0
    _n = list._first

    while _n is not None:
        _n = _n._next
        counter += 1
    if counter == list.size():
        A = True

    if list.size() == 0:
        if list._first is None and list._last is None:
            B = True


    if list.size() != 0:
        if list._last._next is None:
            B = True

    if A and B:
        return True
    else:
        return False




if __name__ == '__main__':
    main()



# Time complexity for all public methods:

# addFirst() - The method only does one comparison, independent of the linked lists size n, so T(n) = 1. (constant)

# addLast() - - Only runs one time so T(n) = 1.

# getFirst() - Only runs one time so T(n) = 1.

# getLast() - Same as above, T(n) = 1.

# Choose "while _counter != index:" as the elementary operation. Since it goes through each element to the searched
# index i, it takes i operations to find the element at index i. However, the worst case scenario, we pick an index
# out of bounds, "if _n is None:" breaks the algorithm which happens after n iterations, so the worst case scenario
# time complexity is T(n) = n.

# removeFirst() - No iterations, T(n) = 1.

# clear() - No iterations, T(n) = 1.

#  size() - No iterations, T(n) = 1.

# string() - Basically the same as the method addLast(), we go through the entire list and add the element to the
# output, so T(n) = n.














