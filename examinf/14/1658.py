def to75(n):
    res = []
    while n > 0:
        res.append(n % 75)
        n //= 75
    return res[::-1]


r = []
for x in range(1, 32001):
    s = to75(75**314 + 75**118 - x)
    r.append(s.count(0))

print(min(r))
