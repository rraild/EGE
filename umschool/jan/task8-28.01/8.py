from itertools import permutations

count = 0
digits = "0123456789"
even = "02468"
odd = "13579"

for p in permutations(digits, 5):
    if p[0] == "0":
        continue

    num = int("".join(p))
    if num % 5 != 0:
        continue

    t = True
    for i in range(4):
        if (p[i] in even) == (p[i + 1] in even):
            t = False
            break

    if t:
        count += 1

print(count)
