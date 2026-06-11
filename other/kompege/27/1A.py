from math import dist

with open("other/kompege/27/27_A_28946.txt") as f:
    points = [list(map(float, s.replace(",", ".").split())) for s in f]

    clusters = []
    eps = 2
    while points:
        clusters.append([points[0]])
        del points[0]
        for p1 in clusters[-1]:
            for p2 in points[:]:
                if dist(p1, p2) < eps:
                    clusters[-1].append(p2)
                    points.remove(p2)

    centroids = [[], []]
    for i in range(len(clusters)):
        min_sum_dist = 100000000000
        for p1 in clusters[i]:
            sum_dist = 0
            for p2 in clusters[i]:
                sum_dist += dist(p1, p2)
            if sum_dist < min_sum_dist:
                min_sum_dist = sum_dist
                centroids[i] = p1

    print(len(clusters[0]), len(clusters[1]))
    print(centroids)
    c = 0
    y_max = 20.98393
    for point in clusters[1]:
        if point[1] < y_max:
            c += 1

    print(c)

    print((centroids[1][0] - centroids[0][0]) * 10_000)
