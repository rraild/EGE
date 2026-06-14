from itertools import product

c = 0
digits = "0123456"
odds = "135"

for w in product(digits, repeat=4):
    if w[0] != "0":
        s = "".join(w)
        if s.count("5") == 1:
            check = True
            for i in range(len(s)):
                if s[i] == "2":
                    if i > 0 and s[i - 1] in odds:
                        check = False
                    if i < len(s) - 1 and s[i + 1] in odds:
                        check = False
            if check:
                c += 1

print(c)
