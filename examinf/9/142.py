l = [[int(d) for d in x.split()] for x in open("other/examinf/9/142.txt")]
count = 0

for x in l:
    povt2 = [d for d in x if x.count(d) == 2]
    povt1 = [d for d in x if x.count(d) == 1]

    if len(povt2) == 2 and len(povt1) == 3:
        x.sort()
        if (x[0] + x[-1]) ** 2 < (x[1] ** 2 + x[2] ** 2 + x[3] ** 2):
            count += 1

print(count)
