f = open("umschool/jun/task26-13.06/2.txt")
n, k = map(int, f.readline().split())

doma = [int(f.readline()) for i in range(n)]
sneguborishiki = []
for s in f:
    power, price = map(int, s.split())
    sneguborishiki.append([price, -power])


doma.sort()
sneguborishiki.sort()
zakupki = []
i = 0
for d in doma:
    while d > abs(sneguborishiki[i][1]):
        i += 1
    zakupki.append([sneguborishiki[i][0], abs(sneguborishiki[i][1])])


print(sum([s[0] for s in zakupki]))
print(max([s[1] for s in zakupki]))
