def v4(n):
    res = ""
    while n > 0:
        res = str(n % 4) + res
        n //= 4
    return res


max_n = 0

for n in range(1, 1000):
    s = v4(n)

    if n % 3 == 0:
        s = s + s[-3:]
    else:
        remainder = n % 3
        added = v4(remainder * 4)
        s = added + s

    r = int(s, 4)

    if r < 1166:
        max_n = max(max_n, n)

print(max_n)
