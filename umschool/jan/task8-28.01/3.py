from itertools import product

count = 0
for p in product("012345", repeat=5):
    if p[0] == "0":
        continue

    if p.count("1") != 1:
        continue

    s = "".join(p)
    if "12" in s or "21" in s:
        continue

    count += 1

print(count)
