from math import dist

with open("other/examinf/27/1627B.txt") as f:
    points = [list(map(float, s.replace(",", ".").split())) for s in f]
    clusters = []
    eps = 0.5
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
P_x = int((sum([x for x, y in best_centroid]) / len(clusters)) * 10_000)
P_y = int((sum([y for x, y in best_centroid]) / len(clusters)) * 10_000)
print(P_x, P_y)
