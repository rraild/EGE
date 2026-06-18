from itertools import product

ct = 0
for i in product(sorted("КОТИА"), repeat=5):
    ct += 1
    d = "".join(s for s in i)
    if ct % 2 != 0:
        if d[0] != "К" and d[0] != "Т":
            if d.count("О") == 2:
                print(ct, d)
