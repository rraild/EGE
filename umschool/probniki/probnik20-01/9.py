c = 0

with open("probniki/probnik20-01/input/9.txt") as f:
    for s in f:
        a = list(map(int, s.strip().split(",")))
        a_sorted = sorted(a)
        mn = a_sorted[0]
        mx = a_sorted[-1]
        rest = a_sorted[1:-1]
        sm = sum(x**2 for x in rest)
        if mx**2 + mn**2 > sm:
            c += 1

print(c)
