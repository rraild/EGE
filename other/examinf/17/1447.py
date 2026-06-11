l = [int(x) for x in open("other/examinf/17/1447.txt")]
ct = 0
mxsm = 0
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        a, b = l[i], l[j]
        usl1 = (a + b) % 18 == 0
        usl2 = (a * b) % 18 == 0
        if (usl1 and not usl2) or (not usl1 and usl2):
            ct += 1
            mxsm = max(mxsm, (a + b))

print(ct, mxsm)
