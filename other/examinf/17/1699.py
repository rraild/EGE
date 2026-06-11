from math import prod

l = [int(x) for x in open("other/examinf/17/1699.txt")]
mx = max(l)
ct = 0
mxpr = -float("inf")
for x in range(len(l) - 2):
    a, b, c = l[x], l[x + 1], l[x + 2]
    ng_sm = abs(sum([d for d in (a, b, c) if d < 0]))
    ps_sm = abs(sum([d for d in (a, b, c) if d > 0]))
    if ng_sm <= ps_sm:
        if abs(prod((a, b, c))) % 10 == abs(mx) % 10:
            ct += 1
            mxpr = max(mxpr, abs(prod((a, b, c))))

print(ct, mxpr)
