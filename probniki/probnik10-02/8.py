from itertools import permutations

l = "СЕРПОАВЫЙ"
v = "ЕОА"
c = "СРПВЫЙ"

ct = 0
for p in permutations(l, 6):
    t = True
    for i in range(5):
        c1 = p[i] in v
        c2 = p[i + 1] in v
        if c1 == c2:
            t = False
            break
    if t:
        ct += 1

print(ct)
