from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(1000000)


@lru_cache(None)
def F(n):
    if n < 65000:
        return F(9 + n) + 13020

    return 4 * (G(n - 4) - 12)


@lru_cache(None)
def G(n):
    if n >= 111700:
        return G(n - 17) + 344

    return 8 * n - 4


for i in range(65100, 1, -1):
    F(i)

for i in range(112000):
    G(i)

print(F(4975))
print((8 + 8 + 9 + 2 + 3 + 3 + 6 + 8) * 2)
