from itertools import permutations

cnt = 0
vowels = "АЕ"
res = set()

for w in permutations("НАГЛЕЖ", 4):
    res.add(w)

for w in res:
    valid = True
    for i in range(len(w) - 1):
        if w[i] in vowels and w[i + 1] in vowels:
            valid = False
            break
    if valid:
        cnt += 1

print(cnt)
