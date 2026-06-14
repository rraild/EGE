import sys

sys.setrecursionlimit(3000)


def F(n):
    if n == 1:
        return 1

    return (n - 1) * F(n - 1)


val = (F(2024) // 7 - F(2023)) / F(2022)
print(val)
