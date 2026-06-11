from itertools import product

count = 0
digits = "01234567"
nechetko = "1357"

for p in product(digits, repeat=5):
    if p[0] == "0":
        continue

    if p.count("4") != 2:
        continue

    t = True
    for i in range(5):
        if p[i] == "4":
            if i > 0 and p[i - 1] in nechetko:
                t = False
                break
            if i < 4 and p[i + 1] in nechetko:
                t = False
                break

    if t:
        count += 1

print(count)
