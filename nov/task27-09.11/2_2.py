from math import dist

f = open("task27-09.11/27_B_2.txt")
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


best_centr = [[], [], []]

for i in range(len(clusters)):
    min_sum_dist = 10**1000

    for c1 in clusters[i]:
        sum_dist = 0
        for p1 in clusters[i]:
            sum_dist += dist(c1, p1)

        if sum_dist < min_sum_dist:
            min_sum_dist = sum_dist
            best_centr[i] = c1

print(best_centr)

p_x = sum([x for x, y in best_centr]) / len(clusters)
p_y = sum([y for x, y in best_centr]) / len(clusters)

print(int(p_x * 10_000), int(p_y * 10_000))
