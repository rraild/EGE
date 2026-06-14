import sys

sys.setrecursionlimit(10000)


def F(n):
    if n < 4:
        return n

    if n >= 4:
        return F(n - 1) + 5 * n**2


print((F(776) + 7 * F(773)) / F(759))
