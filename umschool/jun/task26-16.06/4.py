f = open("umschool/jun/task26-16.06/4.txt")
n, s = map(int, f.readline().split())
a = []
for x in f:
    x = list(map(int, x.split()))
    a += [(x[0], x[-1], sum(x[1:]))]

a.sort(key=lambda x: x[0])
a.sort(key=lambda x: x[1], reverse=True)
a.sort(key=lambda x: x[2], reverse=True)

print(*a[0:s], sep="\n")
