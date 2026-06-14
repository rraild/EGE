import math
import sys
from functools import lru_cache

sys.setrecursionlimit(10000)
sys.set_int_max_str_digits(0)


@lru_cache(None)
def G(n):
    return math.factorial(n)


@lru_cache(None)
def F(n):
    if n <= 7342:
        return G(n)
    if n % 2 == 0:
        return F(n // 3 - 278) + n
    else:
        return F(n - 1) + G(n // 57) + 5


res = F(982134) + G(241)
print(sum(int(d) for d in str(res)))
