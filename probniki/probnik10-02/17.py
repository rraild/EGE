n = [int(x) for x in open("probniki/probnik10-02/17.txt")]

even = [x for x in n if x % 2 == 0]
avg = sum(even) / len(even)

res = []
for i in range(len(n) - 1):
    p1, p2 = n[i], n[i + 1]

    if p1 > avg or p2 > avg:
        if "11" in str(p1) or "11" in str(p2):
            res.append(abs(p1 - p2))

print(len(res), max(res))
