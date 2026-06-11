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


with open("feb/task27.3-08.02/1.txt") as f:
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


visual(clusters)

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

# Px — среднее арифметическое абсцисс центров кластеров, и Py — среднее
# арифметическое ординат центров кластеров.
P_x = (sum([x for x, y in best_centroid]) / len(clusters)) * 10_000
P_y = (sum([y for x, y in best_centroid]) / len(clusters)) * 10_000
print(P_x, P_y)

# P₁ — минимальное расстояние между центром одного кластера и точкой другого
# кластера и P₂ — максимальное расстояние между центром кластера и точкой
# другого кластера.
P1 = min(
    [
        dist(best_centroid[i], p1)
        for i in range(len(clusters))
        for p1 in clusters[1 - i]
    ]
)
P2 = max(
    [
        dist(best_centroid[i], p1)
        for i in range(len(clusters))
        for p1 in clusters[1 - i]
    ]
)
print(int(P1 * 10_000), int(P2 * 10_000))

# P₁ — расстояние между центрами кластеров и P₂ — максимальное расстояние
# между центром каждого кластера и точкой этого же кластера.
P1 = dist(best_centroid[0], best_centroid[1])
P2 = max(
    dist(best_centroid[i], p)
    for i in range(len(clusters))
    for p in clusters[i]
)
print(int(P1 * 10000), int(P2 * 10000))

# Q1 — минимальное расстояние от центра кластера до начала координат, и
# Q2 — максимальное расстояние от центра кластера до начала координат.
dists_to_zero = [dist(c, [0, 0]) for c in best_centroid]
Q1 = min(dists_to_zero)
Q2 = max(dists_to_zero)
print(int(Q1 * 10000), int(Q2 * 10000))

# Q₁ — среднее арифметическое расстояний от центра кластера с минимальным
# количеством точек до точек этого кластера и Q₂ — среднее арифметическое
# расстояний от центра кластера с максимальным количеством точек до точек
# этого кластера.
min_ind, max_ind = clusters.index(min(clusters, key=len)), clusters.index(
    max(clusters, key=len)
)
Q1 = sum([dist(best_centroid[min_ind], p1) for p1 in clusters[min_ind]]) / (
    len(clusters[min_ind]) - 1
)
Q2 = sum([dist(best_centroid[max_ind], p1) for p1 in clusters[max_ind]]) / (
    len(clusters[max_ind]) - 1
)
print(int(Q1 * 10_000), int(Q2 * 10_000))

# Q1 — минимальное расстояние между точками, принадлежащими двум различным
# кластерам, и Q2 — максимальное расстояние между точками, принадлежащими двум
# различным кластерам.
all_dists = [
    dist(p1, p2)
    for i in range(len(clusters))
    for j in range(i + 1, len(clusters))
    for p1 in clusters[i]
    for p2 in clusters[j]
]
Q1 = min(all_dists)
Q2 = max(all_dists)
print(int(Q1 * 10_000), int(Q2 * 10_000))

# Px - минимальную из абсцисс центров кластеров, и Py - минимальную из ординат
# центров кластеров.
px = min(p[0] for p in best_centroid)
py = min(p[1] for p in best_centroid)
print(int(abs(px * 10000)), int(abs(py * 10000)))

# Px — среднее арифметическое абсцисс центров кластеров, и Py — среднее
# арифметическое ординат центров кластеров, а Ps — сумма плотностей кластеров.
P_x = sum([x for x, y in best_centroid]) / len(clusters)
P_y = sum([y for x, y in best_centroid]) / len(clusters)
P_s = sum([len(cluster) / 16 for cluster in clusters]) * 1000
print(int((P_x + P_y) * 10_000), P_s)
