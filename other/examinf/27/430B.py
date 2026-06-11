from math import dist

f = open("other/examinf/27/430B.txt")
f.readline()
points = [list(map(float, s.replace(",", ".").split())) for s in f]


clusters = [[], [], []]

for x, y in points:
    if x > 5:
        clusters[0].append([x, y])

    elif y < 4:
        clusters[1].append([x, y])

    else:
        clusters[2].append([x, y])


best_centoids = [[], [], []]

for i in range(len(clusters)):
    min_sum_dist = 10 * 100000
    for c1 in clusters[i]:
        sum_dist = 0
        for p1 in clusters[i]:
            sum_dist += dist(c1, p1)

        if sum_dist < min_sum_dist:
            min_sum_dist = sum_dist
            best_centoids[i] = c1

print(best_centoids)

p_x = sum([x for x, y in best_centoids]) / len(clusters)
p_y = sum([y for x, y in best_centoids]) / len(clusters)
print(int(p_x * 10_000), int(p_y * 10_000))
