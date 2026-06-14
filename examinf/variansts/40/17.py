l = [int(x) for x in open("other/examinf/variansts/40/1508_1.txt")]
mx4 = max([d for d in l if len(str(abs(d))) == 4])
ct = 0
mnsm = float("inf")
for x in range(len(l) - 1):
    a, b = l[x], l[x + 1]
    usl1 = [d for d in (a, b) if d <= mx4]
    if len(usl1) == 1:
        sm = a**2 + b**2
        if abs(sm) % 100 == 12:
            ct += 1
            mnsm = min(mnsm, sm)

print(ct, mnsm)
