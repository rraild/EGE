from sys import setrecursionlimit

setrecursionlimit(999999)


def F(n):
    if n == 1:
        return 1

    return 2 * n + F(n - 1)


print(F(57693))
print(sum(list(map(int, str(3328539941)))) ** 2)
