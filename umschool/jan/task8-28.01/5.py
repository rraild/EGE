from itertools import product

count = 0
for p in product("012345678", repeat=6):
    nechet = "01357"
    if p[0] in nechet:
        continue

    if p[-1] in "25":
        continue

    if p.count("1") > 1:
        count += 1

print(count)
