from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(5000)


@lru_cache(None)
def F(n):
    if n < 7:
        return 7
    if n % 3 != 0:
        return 5 - F(n - 1)
    return 3 + F(n - 1)


for i in range(3016):
    F(i)

print(F(3015))
