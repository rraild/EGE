from itertools import product

cnt = 0

for w in product("БОТАЙ", repeat=3):
    if w.count("Б") == 1:
        if w[0] != "А" and w[-1] != "Й":
            cnt += 1

print(cnt)
