f = open("umschool/jun/task26-16.06/3.txt")
s, n = map(int, f.readline().split())
a = [int(i) for i in f]
a.sort()
i = 0
while sum(a[: i + 1]) <= s:
    i += 1

print(n - i, sum(a) - sum(a[: i + 1]))
