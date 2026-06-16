f = open("umschool/jun/task26-13.06/3.txt")
n = int(f.readline())
minuts = [0] * 1440
for s in f:
    start, end = map(int, s.split())
    for i in range(start, end):
        minuts[i] += 1

print(max(minuts))
ct = 0
for i in range(len(minuts) - 1):
    if minuts[i] == 643 and minuts[i + 1] != 643:
        ct += 1

print(ct)
