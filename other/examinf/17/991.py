l = [int(x) for x in open("other/examinf/17/991.txt")]
mn7 = min([x for x in l if abs(x) % 10 == 7])
ct = 0
mx = 0
for i in range(len(l) - 2):
    a, b, c = l[i], l[i + 1], l[i + 2]
    usl1 = [x for x in (a, b, c) if len(str(abs(x))) == 5]
    if usl1:
        usl2 = (a * b * c) % mn7 == 0
        if usl2:
            ct += 1
            mx = max(mx, (a * b * c))

print(ct, mx)
