from math import dist

with open("mar/task27-08.03/5B.txt") as f:
    points = [list(map(float, s.replace(",", ".").split())) for s in f]
    clusters = []
    eps = 0.8
    while points:
        clusters.append([points[0]])
        del points[0]
        for p1 in clusters[-1]:
            for p2 in points[:]:
                if dist(p1, p2) < eps:
                    clusters[-1].append(p2)
                    points.remove(p2)

        if len(clusters[-1]) <= 3:
            del clusters[-1]

best_centroid = [[] for _ in range(len(clusters))]
for i in range(len(clusters)):
    min_sum_dist = float("inf")
    for c1 in clusters[i]:
        sum_dist = 0
        for p1 in clusters[i]:
            sum_dist += dist(c1, p1)
        if sum_dist < min_sum_dist:
            min_sum_dist = sum_dist
            best_centroid[i] = c1

print(best_centroid)
print([len(c) for c in clusters])
Q1 = sum([1 for p1 in clusters[0] if 0.5 <= dist(p1, best_centroid[0]) <= 2.5])
Q2 = sum([1 for p1 in clusters[2] if 0.4 <= dist(p1, best_centroid[2]) <= 1.6])
print(Q1, Q2)
