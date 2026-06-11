ans = 0
with open("feb/task9.2-06.02/16.txt") as f:
    for s in f:
        a = sorted(map(int, s.split()))

        c1 = (a[0] + a[3]) ** 2 > (a[1] + a[2]) ** 2
        c2 = len(set(a)) < 4

        if c1 and c2:
            ans += 1
print(ans)
