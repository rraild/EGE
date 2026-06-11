from itertools import product

c = 0
for i in product(sorted("ФУТБЛОКА"), repeat=6):
    c += 1
    if i[0] != "У" and i.count("Ф") == 2 and i.count("А") <= 1:
        print(c, "".join(i))
