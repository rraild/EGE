l = [int(x) for x in open("examinf/17/1700.txt")]

ct = 0
mxsm = []
for i in range(len(l) - 2):
    a, b, c = l[i], l[i + 1], l[i + 2]
    usl1 = [d for d in (a, b, c) if str(d)[0] == str(d)[-1]]
    if len(usl1) == 1:
        usl2 = [d for d in (a, b, c) if len(str(d)) == 4 and str(d)[-3] == "2"]
        if len(usl2) == 2:
            ct += 1
            mxsm.append(max(a, b, c))

print(ct, sum(mxsm))
