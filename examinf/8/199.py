from itertools import product

cnt = 0
for w in product("567", repeat=12):
    ok = True
    for i in range(11):
        if w[i] == "5" and w[i + 1] == "5":
            ok = False
            break
    if ok:
        cnt += 1

print(cnt)
