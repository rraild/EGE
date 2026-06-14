import sys

sys.setrecursionlimit(10000)


def F(n):
    return 3 * G(n - 3) + 11  # type: ignore


def G(n):
    if n < 12:
        return 5 * n

    if n >= 12:
        return G(n - 4) + 7  # type: ignore


print(F(20001))
