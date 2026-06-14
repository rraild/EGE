from itertools import product

letters = "ОЛИВЬЕ"
symbols = letters + "_"
count = 0

for p in product(symbols, repeat=6):
    s = "".join(p)

    pairs = 0
    for i in range(len(s) - 2):
        if s[i] in letters and s[i + 1] == "_" and s[i + 2] in letters:
            pairs += 1

    if pairs >= 2:
        count += 1

print(count)
