from collections import Counter

with open("dec/task9&17-24.12/3.txt") as f:
    ct = 0
    for s in f:
        n = list(map(int, s.split()))
        d = dict(Counter(n))
        if list(d.values()).count(3) == 1 and list(d.values()).count(1) == 4:
            reps = [x for x, c in d.items() if c == 3]
            unrep = [x for x, c in d.items() if c == 1]
            if sum(reps) / len(reps) > max(unrep):
                ct += 1

    print(ct)
