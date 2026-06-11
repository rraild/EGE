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


with open("feb/task27.3-08.02/4.txt") as f:
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

min_ind, max_ind = clusters.index(min(clusters, key=len)), clusters.index(
    max(clusters, key=len)
)

Q1 = sum([dist(best_centroid[min_ind], p1) for p1 in clusters[min_ind]]) / (
    len(clusters[min_ind]) - 1
)

Q2 = sum([dist(best_centroid[max_ind], p1) for p1 in clusters[max_ind]]) / (
    len(clusters[max_ind]) - 1
)

print(Q1, Q2)

print(int(Q1 * 10_000), int(Q2 * 10_000))
