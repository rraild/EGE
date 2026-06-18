l = [[int(d) for d in x.split()] for x in open("examinf/variansts/61/9.txt")]

for x in l:
    povt = [d for d in x if x.count(d) == 2]
    nepovt = [d for d in x if x.count(d) == 1]
    if len(povt) == 2 and len(nepovt) == 4:
        if sum(nepovt) % povt[0] == 0:
            print(sum(x))
