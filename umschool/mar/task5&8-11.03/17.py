from itertools import product

cnt = 0
vowels = "АОИ"
consonants = "ЛГРТМ"

for w in product("АЛГОРИТМ", repeat=7):
    v_cnt = 0
    c_cnt = 0
    for char in w:
        if char in vowels:
            v_cnt += 1
        else:
            c_cnt += 1

    if c_cnt > v_cnt:
        cnt += 1

print(cnt)
