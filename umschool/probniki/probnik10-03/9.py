l = [[int(d) for d in x.split()] for x in open("probniki/probnik10-03/9.txt")]
count = 0

for x in l:
    povt3 = [d for d in x if x.count(d) == 3]
    povt1 = [d for d in x if x.count(d) == 1]
    if len(povt3) == 3 and len(povt1) == 4:
        s = (max(povt1) - min(povt1)) ** 2 < povt3[0] ** 2
        if s:
            count += 1

print(count)
