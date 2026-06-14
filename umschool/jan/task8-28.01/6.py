from itertools import product

c = 0
even = "0246"

for p in product("01234567", repeat=6):
    if p[0] == "0":
        continue

    t = True
    for i in range(5):
        if (p[i] in even) == (p[i + 1] in even):
            t = False
            break

    if t:
        c += 1

print(c)
