ans = 0
l = 0
with open("feb/task9.2-06.02/15.txt") as f:
    for s in f:
        l += 1
        a = list(map(int, s.split()))

        c = [a.count(x) for x in set(a)]
        c1 = c.count(3) == 1 and c.count(1) == 4

        if c1:
            rep = [x for x in a if a.count(x) == 3][0]
            unq = [x for x in a if a.count(x) == 1]

            c2 = (sum(unq) / 4) <= rep

            if c2:
                ans = sum(a)

print(ans)
