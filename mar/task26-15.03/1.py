with open("mar/task26-15.03/1.txt") as f:
    n, m, k = map(int, f.readline().split())
    mesta_info = [m] * (k + 1)

    for _ in range(n):
        ryad, mesto = map(int, f.readline().split())
        mesta_info[mesto] = min(mesta_info[mesto], ryad - 1)

    res = []
    for i in range(1, len(mesta_info) - 1):
        left, right = mesta_info[i], mesta_info[i + 1]
        res.append([min(left, right), i, i + 1])

print(*max(res)[:2])
