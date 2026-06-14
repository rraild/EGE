from itertools import product

count = 0
for p in product("0123456", repeat=5):
    chet = "0246"
    if p[0] in chet:
        continue

    if p[-1] in "15":
        continue

    if p.count("3") <= 1:
        count += 1

print(count)
