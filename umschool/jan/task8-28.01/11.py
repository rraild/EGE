from itertools import product

count = 0
for p in product("ЕГЭ", repeat=5):
    if p.count("Е") == 1:
        count += 1

print(count)
