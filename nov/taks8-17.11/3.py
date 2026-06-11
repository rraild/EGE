from itertools import product

c = 0
for i in product(sorted("БЛАНК"), repeat=6):
    s = "".join(i)
    if s.startswith("К") and s.count("Н") == 2:
        c += 1
        print(c, s)
