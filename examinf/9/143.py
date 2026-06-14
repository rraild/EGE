l = [[int(d) for d in x.split()] for x in open("other/examinf/9/143.txt")]
count = 0

for x in l:
    povt2 = [d for d in x if x.count(d) == 2]
    povt1 = [d for d in x if x.count(d) == 1]

    if len(povt2) == 2 and len(povt1) == 2:
        x.sort()
        sum_max2 = x[2] + x[3]
        sum_min2 = x[0] + x[1]

        if sum_max2 > 2 * sum_min2:
            if x[3] % x[0] != 0:
                count += 1

print(count)
