import sys

sys.setrecursionlimit(10000)


def F(n):
    if n <= 3:
        return 1

    if n > 3:
        return (n + 3) * F(n - 2)


print(F(2030) / F(2024))
