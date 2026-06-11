l = [
    [int(d) for d in x.split()]
    for x in open("other/examinf/variansts/40/9.txt")
]
count = 0

for x in l:
    usl1 = [d for d in x if x.count(d) == 3 and d == max(x)]
    usl2 = [d for d in x if x.count(d) == 1]
    if len(usl1) == 3 and len(usl2) == 4:
        print(sum(x) / len(x))
