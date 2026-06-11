from math import dist

with open("mar/task27-08.03/4B.txt") as f:
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

        if len(clusters[-1]) <= 3:
            del clusters[-1]

anti_centroid = [[] for _ in range(len(clusters))]
for i in range(len(clusters)):
    max_sum_dist = -float("inf")
    for c1 in clusters[i]:
        sum_dist = 0
        for p1 in clusters[i]:
            sum_dist += dist(c1, p1)
        if sum_dist > max_sum_dist:
            max_sum_dist = sum_dist
            anti_centroid[i] = c1

print(anti_centroid)
P_x = (sum([x for x, y in anti_centroid]) / len(clusters)) * 10_000
P_y = (sum([y for x, y in anti_centroid]) / len(clusters)) * 10_000
print(P_x, P_y)
