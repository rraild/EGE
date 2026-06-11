from itertools import product

c = 0
for i in product(sorted("FORK"), repeat=6):
    s = "".join(i)
    if s.count("R") >= 1:
        c += 1
        print(c, s)
