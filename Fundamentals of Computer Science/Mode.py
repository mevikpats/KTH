import math

def mode(vec):
    """Returns the most common element in a list of integers.
     If several integers occurs the same amount of times it returns the smallest.
      """
    dict = {}
    count = 0
    value = 2**64

    for i in vec: # O(n)
        if i in dict.keys():
            dict[i] += 1 # O(1)
        else:
            dict[i] = 1 # O(1)
    print(dict)

    for j in dict: #O(n)
        if (dict[j] > count) or ((dict[j] == count) and j < value):
            count = dict[j] # O(1)
            value = j # O(1)

    return value


# Unit test
def main():
    v1 = [1,3,5,3,2]
    v2 = [3,2,5,7,2,5]
    v3 = [-1,-3,7,-3]
    v4 = [-4,2,1,2,-4]
    assert mode(v1) == 3
    assert mode(v2) == 2
    assert mode(v3) == -3
    assert mode(v4) == -4
