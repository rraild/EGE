from itertools import product

c = 1
for i in product(sorted("YEA"), repeat=5):
    if c == 50:
        print(c, "".join(i))
        break
    c += 1
