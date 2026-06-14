from math import dist


def visual(cluesters):
    from turtle import done, dot, setpos, tracer, up

    up()
    tracer(0)
    colors = ["green", "blue", "red"]
    k = 10

    for i in range(len(cluesters)):
        for x, y in cluesters[i]:
            setpos(x * k, y * k)
            dot(5, colors[i])

    done()


with open("feb/task27.3-08.02/5.txt") as f:
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

        if len(clusters[-1]) <= 3:
            del clusters[-1]


visual(clusters)

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

all_dists = [
    dist(p1, p2)
    for i in range(len(clusters))
    for j in range(i + 1, len(clusters))
    for p1 in clusters[i]
    for p2 in clusters[j]
]

Q1 = min(all_dists)
Q2 = max(all_dists)

print(int(Q1 * 10_000), int(Q2 * 10_000), sep="")
