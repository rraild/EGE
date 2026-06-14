from math import dist

f = open("other/examinf/27/1451B.txt")
points = [list(map(float, s.replace(",", ".").split())) for s in f]
eps = 5
clusters = []
while points:
    clusters.append([points[0]])
    del points[0]
    for p1 in clusters[-1]:
        for p2 in points[:]:
            if dist(p1, p2) < eps:
                clusters[-1].append(p2)
                points.remove(p2)

    if len(clusters[-1]) <= 20:
        del clusters[-1]

kraya = [[], [], [], [], []]
for i in range(len(clusters)):
    max_sum_dist = -10000000000000
    for p1 in clusters[i]:
        sum_dist = 0
        for p2 in clusters[i]:
            sum_dist += dist(p1, p2)
        if sum_dist > max_sum_dist:
            max_sum_dist = sum_dist
            kraya[i] = p1

print(kraya)
P_x = (sum([x for x, y in kraya]) / len(clusters)) * 10_000
P_y = (sum([y for x, y in kraya]) / len(clusters)) * 10_000
print(int(P_x), int(P_y))
