from math import dist

with open("other/kompege/27/27_B_28946.txt") as f:
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

    centroids = [[], [], []]
    for i in range(len(clusters)):
        min_sum_dist = 100000000000
        for p1 in clusters[i]:
            sum_dist = 0
            for p2 in clusters[i]:
                sum_dist += dist(p1, p2)
            if sum_dist < min_sum_dist:
                min_sum_dist = sum_dist
                centroids[i] = p1

    print(len(clusters[0]), len(clusters[1]), len(clusters[2]))
    ct = 0
    for point in clusters[2]:
        min_x = centroids[2][0] - 1.8 / 2
        max_x = centroids[2][0] + 1.8 / 2
        min_y = centroids[2][1] - 1.8 / 2
        max_y = centroids[2][1] + 1.8 / 2

        if min_x <= point[0] <= max_x and min_y <= point[1] <= max_y:
            ct += 1
    print(ct)

    print((centroids[0][1] - centroids[1][1]) * 10_000)
