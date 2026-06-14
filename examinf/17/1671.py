l = [int(d) for d in open("other/examinf/17/1671.txt")]
mx37 = max([d for d in l if d % 100 == 37])
ct = 0
total_sum = 0

for i in range(len(l) - 3):
    four = [l[i], l[i + 1], l[i + 2], l[i + 3]]
    usl1 = [d for d in four if d > mx37]
    if len(usl1) == 2:
        usl2 = [d for d in four if d % 10 == (d // 10) % 10]
        if len(usl2) == 1:
            ct += 1
            total_sum += usl2[0]

print(ct, total_sum)
