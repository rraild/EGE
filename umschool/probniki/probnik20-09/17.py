f = open("input.txt")
a = list(map(int, f.read().split()))
m = min(a)
c = 0
mx = 0
for i in range(len(a) - 1):
    if a[i] % 123 == m or a[i + 1] % 123 == m:
        c += 1
        mx = max(mx, a[i] + a[i + 1])
print(str(c) + str(mx))
