def to_3(n):
    s = ""
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    return s


res = []

for n in range(11, 1000):
    s = to_3(n)

    chet = sum(1 for c in s if int(c) % 2 == 0)
    nechet = len(s) - chet

    if chet > nechet:
        s = "22" + s
    else:
        s = "11" + s

    r = int(s, 3)
    if r > 100:
        res.append(r)

print(min(res))
