from math import ceil

with open("dec/task26-07.12/1.txt") as f:
    n = int(f.readline())
    a = [int(s) for s in f]
    a120 = [x for x in a if x > 120]
    a120.sort()
    sale = sum(a120[: len(a120) // 2]) * 0.25
    print(ceil(sum(a) - sale), max(a120[: len(a120) // 2]))
