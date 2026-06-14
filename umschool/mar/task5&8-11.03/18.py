from itertools import product

cnt = 0
digits = "012345"

for w in product(digits, repeat=4):
    if w[0] != "0":
        s = "".join(w)
        if s.count("1") == 1:
            if "14" not in s and "41" not in s:
                cnt += 1

print(cnt)
