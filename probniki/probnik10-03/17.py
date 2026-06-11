def f(n, b):
    s = ""
    while n > 0:
        s = str(n % b) + s
        n //= b
    return s


l = [int(x) for x in open("probniki/probnik10-03/17.txt")]
mx69 = max([x for x in l if abs(x) % 69 == 0])
mn81 = min([x for x in l if abs(x) % 81 == 0])
ct = 0
mxsm = 0
for x in range(len(l) - 1):
    a, b = l[x], l[x + 1]
    if (a > mx69 and b < mn81) or (b > mx69 and a < mn81):
        ct += 1
        if int(f(a + b, 8)[-1]) % 2 == 0:
            mxsm = max(mxsm, (a + b))

print(ct, mxsm)
