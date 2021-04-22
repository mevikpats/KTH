def sort(vec):
    """Sorts a vector such that it's negative elements comes first."""
    try:
        a = 0
        for i in range(len(vec)): #O(n)
            if vec[i] < 0:
            # //Invariant: Every negative element is moved from it's initial index
            # to the right of the previous negative element. The first negative element
            # that is found is moved to the beginning from it's initial index.
                temp = vec[i] #O(1)
                vec[i] = vec[a] #O(1)
                vec[a] = temp #O(1)
                a += 1
    except:
        return None

#unit test
def main():
    V = [-3, 2, 10, -5, -3]
    exp_V = [-3, -5, -3, 2, 10]
    sort(V)
    assert exp_V == V

    W = [-3, -2, -5, -10, -4]
    exp_W = W
    sort(W)
    assert exp_W == W

    U = [3, 2, 5, 10, 4]
    exp_U = U
    assert exp_U == U

    T = [1, 'Kaffe', 3, -2]
    assert sort(T) is None

if __name__ == '__main__':
    main()



