from math import dist

with open("examinf/variansts/61/27_B.txt") as f:
    points = [list(map(float, s.replace(",", ".").split())) for s in f]
    clusters = []
    eps = 3
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
    print(len(clusters[i]))
    min_sum_dist = float("inf")
    for p1 in clusters[i]:
        sum_dist = 0
        for p2 in clusters[i]:
            sum_dist += dist(p1, p2)
        if sum_dist < min_sum_dist:
            min_sum_dist = sum_dist
            best_centroid[i] = p1

print(best_centroid)

mx_dist = -float("inf")
for i in range(len(clusters)):
    for point in clusters[i]:
        cur_dist = dist(point, best_centroid[i])
        mx_dist = max(mx_dist, cur_dist)


print(
    int(dist(best_centroid[0], best_centroid[2]) * 10_000),
    int(mx_dist * 10_000),
)
