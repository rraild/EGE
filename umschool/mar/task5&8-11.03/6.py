def to_tri(n):
    res = ""
    while n > 0:
        res = str(n % 3) + res
        n //= 3
    return res


results = []

for n in range(1, 1000):
    s = to_tri(n)

    if n % 3 == 0:
        s = s + s[:2]
    else:
        rem_val = (n % 3) * 7
        s = s + to_tri(rem_val)

    r = int(s, 3)
    if r > 260:
        results.append(r)

print(min(results))
