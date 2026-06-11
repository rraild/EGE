from itertools import product

count = 0
digits = "01234567"

for p in product(digits, repeat=5):
    if p[0] == "0":
        continue

    if p[0] in "1357":
        continue

    if p[-1] in "34":
        continue

    if p.count("5") > 1:
        continue

    count += 1

print(count)
