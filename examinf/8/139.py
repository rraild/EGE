from itertools import product

cnt = 0
i = 0

for w in product("БЖОУФЦЮ", repeat=4):
    i += 1
    if i % 2 == 0 and w[0] == "Ж" and w[1] == "О":
        cnt += 1

print(cnt)
