from math import prod

l = [int(d) for d in open("examinf/variansts/61/17.txt")]
ct = 0
mnpr = float("inf")
mx3 = max([d for d in l if len(str(d)) == 3])
for i in range(len(l) - 1):
    a, b = l[i], l[i + 1]
    usl1 = [d for d in (a, b) if len(str(d)) == 3]
    if len(usl1) == 1:
        usl2 = prod((a, b)) % mx3 == 0
        if usl2:
            ct += 1
            mnpr = min(prod((a, b)), mnpr)


print(ct, mnpr)
