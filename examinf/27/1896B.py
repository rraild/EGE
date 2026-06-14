from math import dist

with open("other/examinf/27/1896B.txt") as f:
    points = [list(map(float, s.replace(",", ".").split())) for s in f]
    clusters = []
    eps = 1
    while points:
        clusters.append([points[0]])
        del points[0]
        for p1 in clusters[-1]:
            for p2 in points[:]:
                if dist(p1, p2) < eps:
                    clusters[-1].append(p2)
                    points.remove(p2)


best_centroid = [[] for _ in range(len(clusters))]
for i in range(len(clusters)):
    min_sum_dist = float("inf")
    for p1 in clusters[i]:
        sum_dist = 0
        for p2 in clusters[i]:
            sum_dist += dist(p1, p2)

        if sum_dist < min_sum_dist:
            min_sum_dist = sum_dist
            best_centroid[i] = p1


print(best_centroid)
print(len(clusters[0]), len(clusters[1]), len(clusters[2]))


ct = 0
for p in clusters[1]:
    if best_centroid[1][0] - 1 <= p[0] <= best_centroid[1][0] + 1:
        if best_centroid[1][1] - 1 <= p[1] <= best_centroid[1][1] + 1:
            ct += 1

print(ct)
print(int((best_centroid[0][1] - best_centroid[2][1]) * 10_000))
