from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(10000000)


@lru_cache(None)
def F(n):
    if n >= 321000:
        return 1
    return F(n + 3) + 7


@lru_cache(None)
def G(n):
    if n < 10:
        return n
    return G(n - 3) + 5


for i in range(322000, 1, -1):
    F(i)
for i in range(1, 322000):
    G(i)
print(F(15) - G(3000))
