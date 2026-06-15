from math import dist

with open("examinf/27/1899B.txt") as f:
    points = [
        [
            float(s.replace(",", ".").split()[0]),
            float(s.replace(",", ".").split()[1]),
            s.split()[2],
        ]
        for s in f
    ]
    clusters = []
    eps = 1
    while points:
        clusters.append([points[0]])
        del points[0]
        for p1 in clusters[-1]:
            for p2 in points[:]:
                if dist(p1[0:2], p2[0:2]) < eps:
                    clusters[-1].append(p2)
                    points.remove(p2)


best_centroid = [[] for _ in range(len(clusters))]
for i in range(len(clusters)):
    min_sum_dist = float("inf")
    for p1 in clusters[i]:
        sum_dist = 0
        for p2 in clusters[i]:
            sum_dist += dist(p1[0:2], p2[0:2])
        if sum_dist < min_sum_dist:
            min_sum_dist = sum_dist
            best_centroid[i] = p1


mx = []
for p in clusters[0]:
    if p[2][0] == "J" and p[2][2:] == "V":
        mx.append(p[0])

mn = []
for p in clusters[2]:
    if p[2][0] == "J" and p[2][2:] == "V":
        mn.append(p[1])

print(int(max(mx) * 10_000), int(max(mn) * 10_000))
