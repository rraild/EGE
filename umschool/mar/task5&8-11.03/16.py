from itertools import product

cnt = 0
for w in product("123456", repeat=4):
    if w.count("4") == 1:
        ev = 0
        od = 0
        for x in w:
            if int(x) % 2 == 0:
                ev += 1
            else:
                od += 1

        if ev <= od:
            cnt += 1

print(cnt)
