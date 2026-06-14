from math import dist

with open("other/examinf/27/1811B.txt") as f:
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


print(best_centroid)


dists = []
for i in range(len(clusters)):
    for point in clusters[i]:
        if "L" in point[-1] and "V" == point[-1][-1]:
            cur_dist = dist(best_centroid[i][0:2], point[0:2])
            dists.append(cur_dist)

print(int(min(dists) * 10_000), int(max(dists) * 10_000))
