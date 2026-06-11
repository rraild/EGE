from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(100000)


@lru_cache(None)
def F(n):
    return 2 * (G(n - 2) + 9)


@lru_cache(None)
def G(n):
    if n < 20:
        return 2 * n

    return G(n - 2) + 3


for i in range(1, 20000):
    F(i)

print(F(16888))
