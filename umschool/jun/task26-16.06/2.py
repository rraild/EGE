f = open("umschool/jun/task26-16.06/2.txt")
n, k, m = map(int, f.readline().split())

a = [int(i) for i in f]
a.sort(reverse=True)
print(a[m + k])
print(sum(a[:k]) * 0.2 + sum(a[k : m + k]) * 0.1)
