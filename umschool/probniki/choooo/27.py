from math import dist

f = open("probniki/choooo/27A.txt")
points = [list(map(float, s.replace(",", ".").split())) for s in f]
eps = 1
clusters = []
while points:
    clusters.append([points[0]])
    del points[0]
    for p1 in clusters[-1]:
        for p2 in points[:]:
            if dist(p1, p2) < eps:
                clusters[-1].append(p2)
                points.remove(p2)

centroids = [[], [], [], []]
for i in range(len(clusters)):
    min_sum_dist = 1000000000
    for p1 in clusters[i]:
        sum_dist = 0
        for p2 in clusters[i]:
            sum_dist += dist(p1, p2)
        if sum_dist < min_sum_dist:
            min_sum_dist = sum_dist
            centroids[i] = p1

P_x = (sum([x for x, y in centroids]) / len(clusters)) * 10_000
P_y = (sum([y for x, y in centroids]) / len(clusters)) * 10_000
print(int(P_x), int(P_y))
