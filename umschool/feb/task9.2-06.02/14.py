ans = 0
with open("feb/task9.2-06.02/14.txt") as f:
    for s in f:
        a = sorted(map(int, s.split()))

        c1 = a[0] + a[3] == a[1] + a[2]

        c2 = (a[3] - a[0]) > abs((a[1] + a[2]) - a[3])

        if c1 and c2:
            ans += 1
print(ans)
