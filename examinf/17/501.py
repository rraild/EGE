l = [int(x) for x in open("other/examinf/17/501.txt")]
kr32 = len([x for x in l if abs(x) % 32 == 0])
ct = 0
mx = 0
for i in range(len(l) - 1):
    a, b = l[i], l[i + 1]
    usl1 = [x for x in (a, b) if x < 0]
    if usl1:
        usl2 = (a + b) < kr32
        if usl2:
            ct += 1
            mx = max(mx, (a + b))

print(ct, mx)
