from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(100000)


@lru_cache(None)
def F(n):
    if n >= 3000:
        return n

    return n + 5 + F(n + 2)


for i in range(150, 1, -1):
    F(i)

print(F(108) - F(112))
