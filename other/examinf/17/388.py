l = [int(x) for x in open("other/examinf/17/388.txt")]
mx17 = max([x for x in l if abs(x) % 100 == 17])
ct = 0
mxsm = 0
for x in range(len(l) - 2):
    a, b, c = l[x], l[x + 1], l[x + 2]
    usl1 = [x for x in (a, b, c) if len(str(abs(x))) == 4]
    if len(usl1) == 2:
        usl2 = [x for x in (a, b, c) if x % 5 == 0]
        if usl2:
            if sum((a, b, c)) > mx17:
                ct += 1
                mxsm = max(mxsm, sum((a, b, c)))

print(ct, mxsm)
