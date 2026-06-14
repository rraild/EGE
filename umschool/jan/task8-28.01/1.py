from itertools import product

c = 0

for p in product("0123456", repeat=4):
    if p[0] == "0":
        continue

    if int(p[0]) % 2 == 0:
        continue

    if p.count("4") == 1:
        c += 1

print(c)
