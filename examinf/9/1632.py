l = [[int(d) for d in x.split()] for x in open("other/examinf/9/1632.txt")]
ct = 0

for x in l:
    ct += 1
    povt = [d for d in x if x.count(d) > 1]
    nepovt = [d for d in x if x.count(d) == 1]
    if povt and nepovt:
        if sum(povt) ** 2 > sum(nepovt) ** 2:
            if sum(x) % 2 != 0:
                print(ct)
