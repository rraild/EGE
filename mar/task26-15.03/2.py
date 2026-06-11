with open("mar/task26-15.03/2.txt") as f:
    n, m, k = map(int, f.readline().split())
    mesta = [[] for _ in range(k + 1)]

    for _ in range(n):
        ryad, m = map(int, f.readline().split())
        mesta[m].append(ryad)

    res = []
    for i in range(1, len(mesta)):
        mesta[i] = sorted([0] + mesta[i] + [m + 1], reverse=True)
        for j in range(len(mesta[i]) - 1):
            up, down = mesta[i][j], mesta[i][j + 1]
            res.append([up - down - 1 - 1, -(up - 1)])

print(max(res)[::-1])
