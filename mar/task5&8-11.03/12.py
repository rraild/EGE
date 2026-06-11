from itertools import product

cnt = 0
for w in product("СМАРТ", repeat=6):
    s = "".join(w)

    if s.count("Р") <= 1:
        if s[0] != "Р" and s[-1] != "Р":
            if "РТ" not in s and "ТР" not in s:
                cnt += 1

print(cnt)
