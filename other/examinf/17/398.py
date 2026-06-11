l = [int(x) for x in open("other/examinf/17/398.txt")]
mx7 = max([x for x in l if abs(x) % 10 == 7])
ct = 0
t = []
for x in range(len(l) - 2):
    a, b, c = l[x], l[x + 1], l[x + 2]
    e = [x for x in (a, b, c) if x % 2 != 0]
    check = [x for x in (a, b, c) if x > mx7]
    if len(e) == 2 and len(check) == 1:
        ct += 1
        t.append(a)
        t.append(b)
        t.append(c)

sr = sum(set(t)) / (len(set(t)))
print(ct, str(sr)[:3])
