from collections import Counter

with open("dec/task9&17-24.12/13+.txt") as f:
    ct = 0
    for s in f:
        n = list(map(int, s.split()))
        d = dict(Counter(n))
        reps = [x for x in n if d[x] > 1]
        unrep = [x for x, c in d.items() if c == 1]
        if len(reps) != int(len(n) / 2):
            continue

        if unrep and max(unrep) ** 2 > sum(reps) ** 2:
            ct += 1

    print(ct)
