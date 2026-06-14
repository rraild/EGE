from itertools import product

cnt = 0
alphabet = "SETUP"
restricted = "SET"

for w in product(alphabet, repeat=6):
    s = "".join(w)

    if s.count("U") >= 1:
        valid = True
        for i in range(len(s) - 1):
            if s[i] in restricted and s[i + 1] in restricted:
                valid = False
                break

        if valid:
            cnt += 1

print(cnt)
