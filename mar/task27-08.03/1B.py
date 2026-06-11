from math import dist


def visual(cluesters):
    from turtle import done, dot, setpos, tracer, up

    up()
    tracer(0)
    colors = ["green", "blue", "red"]
    k = 15

    for i in range(len(cluesters)):
        for x, y in cluesters[i]:
            setpos(x * k, y * k)
            dot(5, colors[i])

    done()


with open("mar/task27-08.03/1B.txt") as f:
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

        if len(clusters[-1]) <= 3:
            del clusters[-1]


# visual(clusters)

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

P_x = (sum([x for x, y in best_centroid]) / len(clusters)) * 10_000
P_y = (sum([y for x, y in best_centroid]) / len(clusters)) * 10_000
print(abs(P_x), abs(P_y))
