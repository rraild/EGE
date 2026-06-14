from math import dist

with open("mar/task27-08.03/5A.txt") as f:
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
p1_point = [-2.2, 0.0]
p2_point = [0.0, -2.0]

p1_val = min(dist(p1_point, c) for c in best_centroid)
p2_val = max(dist(p2_point, c) for c in best_centroid)

print(int(p1_val * 10_000), int(p2_val * 10_000))
