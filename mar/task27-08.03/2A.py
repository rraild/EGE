import math

with open("mar/task27-08.03/2A.txt") as f:
    points = [list(map(float, s.replace(",", ".").split())) for s in f]

clusters = []
eps = 1
while points:
    curr = [points.pop(0)]
    for p1 in curr:
        for p2 in points[:]:
            if math.dist(p1, p2) < eps:
                curr.append(p2)
                points.remove(p2)
    if len(curr) > 3:
        clusters.append(curr)

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
