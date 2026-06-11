d = [[int(d) for d in x.split()] for x in open("probniki/probnik10-02/9.txt")]

c = 0
for x in d:
    povt2 = [c for c in x if x.count(c) == 2]
    povt1 = [c for c in x if x.count(c) == 1]

    if len(povt2) == 4 and len(povt1) == 3:
        if sum(povt2) / 4 >= sum(povt1) / 3:
            c += 1
            print(c, x)

print(c)
