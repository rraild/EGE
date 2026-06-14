f = open("jun/task26-13.06/1.txt")
n = int(f.readline())
a = [int(s) for s in f]
a120 = [x for x in a if x > 120]
a120.sort()
sale = sum(a120[: len(a120) // 2]) * 0.25
# print(len(a120), len(a120[: len(a120) // 2]))

print(sum(a) - sale, max(a120[: len(a120) // 2]))
