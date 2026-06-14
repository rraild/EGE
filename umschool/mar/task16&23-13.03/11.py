from functools import lru_cache


@lru_cache(None)
def F(n):
    if n <= 19:
        return n**3 + 22
    if n % 3 == 0:
        return F(n - 4) + F(n - 8)
    else:
        return F(n - 9) + n + 7


def ch7(num):
    s = str(num)
    for digit in "13579":
        if digit in s:
            return False
    return True


count = 0
for n in range(1, 101):
    if ch7(F(n)):
        count += 1

print(count)
