d = [[int(d) for d in x.split()] for x in open("other/examinf/9/1049.txt")]

for i, a in enumerate(d, 1):
    c = [a.count(x) for x in set(a)]

    c1 = c.count(3) == 2 and c.count(1) == 1

    if c1:
        rep = [x for x in a if a.count(x) == 3]
        unq = [x for x in a if a.count(x) == 1][0]

        avg_rep = sum(rep) / len(rep)

        if avg_rep > unq:
            print(i)
            break
