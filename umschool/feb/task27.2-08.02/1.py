import math

with open("feb/task27.2-08.02/1.txt") as f:
    points = [list(map(float, s.replace(",", ".").split())) for s in f]

clusters = []
eps = 2

while points:
    c = [points.pop(0)]
    i = 0
    while i < len(c):
        p1 = c[i]
        j = 0
        while j < len(points):
            p2 = points[j]
            if math.dist(p1, p2) < eps:
                c.append(points.pop(j))
            else:
                j += 1
        i += 1
    if len(c) > 2:
        clusters.append(c)

centroids = []
for cl in clusters:
    min_s = float("inf")
    best_p = cl[0]
    for p1 in cl:
        s = sum(math.dist(p1, p2) for p2 in cl)
        if s < min_s:
            min_s = s
            best_p = p1
    centroids.append(best_p)

px = min(p[0] for p in centroids)
py = min(p[1] for p in centroids)

print(int(abs(px * 10000)), int(abs(py * 10000)))
