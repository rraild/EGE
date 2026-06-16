f = open("umschool/jun/task26-16.06/1.txt")
n = int(f.readline())
a = [int(i) for i in f]
a.sort(reverse=True)
b = [a[0]]
for i in range(n):
    if a[i] + 8 <= b[-1]:
        b += [a[i]]


print(len(b), b[-1])
