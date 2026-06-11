import math

with open("mar/task27-08.03/2B.txt") as f:
    f.readline()
    points = [list(map(float, s.replace(",", ".").split())) for s in f]

    clusters = [[], [], []]

    for x, y in points:
        if x < -0.75:
            clusters[0].append((x, y))
        elif -0.75 <= x < 2 and y < 0:
            clusters[1].append((x, y))
        else:
            clusters[2].append((x, y))

    dMin, dMax = float("inf"), -float("inf")

    for i in range(len(clusters)):
        for j in range(i + 1, len(clusters)):
            for p1 in clusters[i]:
                for p2 in clusters[j]:
                    d = math.dist(p1, p2)
                    if d < dMin:
                        dMin = d
                    if d > dMax:
                        dMax = d

print(int(dMin * 10000), int(dMax * 10000))
