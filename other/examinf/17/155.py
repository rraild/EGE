l = [int(x) for x in open("other/examinf/17/155.txt")]
min_ev = min([x for x in l if x % 2 == 0])

ct = 0
mnsm = 20001

for x in range(len(l) - 2):
    a, b, c = l[x], l[x + 1], l[x + 2]
    usl1 = [x for x in (a, c) if x % 2 == 0]

    if len(usl1) == 1:
        if b % min_ev == 0:
            ct += 1
            mnsm = min(mnsm, a + c)

print(ct, mnsm)
