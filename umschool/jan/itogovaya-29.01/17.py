from itertools import product

count = 0
digits = "012345678"

for p in product(digits, repeat=6):
    if p[0] == "0":
        continue

    if p[0] in "1357":
        continue

    if p[-1] in "25":
        continue

    if p.count("1") < 2:
        continue

    count += 1

print(count)
