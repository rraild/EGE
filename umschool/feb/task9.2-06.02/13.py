ans = 0
with open("feb/task9.2-06.02/13.txt") as f:
    for s in f:
        a = sorted(map(int, s.split()))

        counts = [a.count(x) for x in set(a)]
        c1 = counts.count(2) == 2 and counts.count(1) == 4

        c2 = a.count(min(a)) == 2

        if c1 and c2:
            ans += 1
print(ans)
