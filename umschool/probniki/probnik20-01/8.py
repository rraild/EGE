def s7(n):
    r = ""
    while n > 0:
        r = str(n % 7) + r
        n //= 7
    return r


c = 0
for i in range(1, 10000):
    n = s7(i)
    if len(n) == 4 and n.count("5") == 1:
        ok = True
        for j in range(3):
            if (n[j] in "135" and n[j + 1] == "2") or (
                n[j + 1] in "135" and n[j] == "2"
            ):
                ok = False
        if ok:
            c += 1

print(c)
