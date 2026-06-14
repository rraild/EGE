from itertools import product

c = 0
digits = "01234567"
starts = "1357"
ends = "123456"

for w in product(digits, repeat=4):
    if w[0] in starts:
        if w[-1] in ends:
            if w.count("5") <= 1:
                c += 1

print(c)
