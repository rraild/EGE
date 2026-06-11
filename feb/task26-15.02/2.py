with open("feb/task26-15.02/2.txt") as f:
    n = int(f.readline())
    data = []
    for s in f:
        start, end = map(int, s.split())
        data.append([end, start])

    data.sort()
    zal = 0
    podoshel = []
    for end, start in data:
        if start >= zal:
            zal = end
            podoshel.append([start, end])

        if start >= 1361:
            print(start, end)

print(len(podoshel), podoshel)
# 40
# 1400
