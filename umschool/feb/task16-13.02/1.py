from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(100000)


@lru_cache(None)
def F(n):
    if n == 1:
        return 1

    return (2 * n - 2) * F(n - 1)


for i in range(1, 3030):
    F(i)

print(F(3029) / F(3027))
