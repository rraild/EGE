from itertools import product

c = 0
r = 0
for i in product(sorted("МОНТАЖЕР"), repeat=6):
    c += 1
    if i[0] == "О" and c % 3 == 0:
        if i.count("Ж") == 2 or i.count("Ж") == 3:
            r += 1
            print(r, "".join(i))
