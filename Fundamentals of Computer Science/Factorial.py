def fac(n):
    """Returns the factorial of n, n! = n * (n-1) * ... * 1, where n is a non negative integer"""
    if n < 0 or not isinstance(n, int):
        return ValueError
    if n == 0:
        return 1
    return n * fac(n-1)

# Unit test
def main():
    assert fac(-3.14) == ValueError
    assert fac(-1) == ValueError
    assert fac(0) == fac(1) == 1
    assert fac(5) == 120
    assert fac(22/7) == ValueError


if __name__ == '__main__':
    main()


#  Proof by induction:
#
#  Base case:
#   P(0) is True since fac(0) returns 1.
#
#  Induction step:
#   Assume that P(i) is true for all i < k. If k ≥ 2 then fac(k) returns k * fac(k-1).
#   According to our induction step, fac(k-1) returns (k-1)! = (k-1) * (k-2) * ... * 1,
#   thus fac(k) will return k * (k-1)! = k!.