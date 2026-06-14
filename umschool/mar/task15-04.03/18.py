B = list(range(100, 120 + 1))
c = 0

for A in range(1, 1000):
    t = True
    for x in range(1, 1000):
        f = (x in B) <= (((x % 35 == 0) == (x % A == 0)) or (x % A == 0))
        if not f:
            t = False
            break
    if t:
        c += 1

print(c)
