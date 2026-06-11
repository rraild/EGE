import sys

sys.setrecursionlimit(10000)


def F(n):
    return 2 * (G(n - 2) + 9)  # type: ignore


def G(n):
    if n < 20:
        return 2 * n

    if n >= 12:
        return G(n - 2) + 3  # type: ignore


print(F(16888))
