from itertools import product

c = 0
for i in product(sorted("РУМБА"), repeat=5):
    c += 1
    if i[0] == "Р":
        print(c, "".join(i))
        break
