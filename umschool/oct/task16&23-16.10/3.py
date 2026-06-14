import sys

sys.setrecursionlimit(10000)


def F(n):
    if n >= 2025:
        return n * n

    if n < 2025:
        return F(n + 3) + n // 4


print(F(2012) - F(2016))
