from itertools import product

c = 1
for i in product(sorted("CANDY"), repeat=4):
    if "".join(i) == "ANDY":
        print(c, "".join(i))
        break
    c += 1
