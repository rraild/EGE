def f(n, b):
    d = []
    while n > 0:
        d.append(n % b)
        n //= b
    return d


v = 8**1006 + 5**1947 + 505
res = f(v, 7)

s6 = res.count(6) * 6
s2 = res.count(2) * 2

print(s6 - s2)
