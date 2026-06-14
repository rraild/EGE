ans = 0
with open("feb/task9.2-06.02/19.txt") as f:
    for s in f:
        a = list(map(int, s.split()))

        ev = [x for x in a if x % 2 == 0]
        od = [x for x in a if x % 2 != 0]

        c1 = len(ev) % 2 == 0 and len(od) % 2 == 0

        c2 = False
        if od:
            c2 = max(od) % 3 == 0

        if c1 and c2:
            ans += 1
print(ans)
