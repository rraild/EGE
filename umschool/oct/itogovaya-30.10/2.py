import sys

sys.setrecursionlimit(10000)


def F(n):
    if n == 1:
        return 1
    return (2 * n - 2) * F(n - 1)


print(F(3029) // F(3027))
