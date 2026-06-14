from itertools import permutations

cnt = 0
res = set()

for w in permutations("ВАРЕНЬЕ", 5):
    res.add(w)

for w in res:
    valid = True
    for i in range(len(w) - 1):
        if w[i] == w[i + 1]:
            valid = False
            break
    if valid:
        cnt += 1

print(cnt)
