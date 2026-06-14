from collections import Counter

with open("dec/task9-22.12/4.txt") as f:
    ct = 0
    for s in f:
        n = list(map(int, s.split()))
        if len(set(n)) == 4:
            d = dict(Counter(n))
            reps = [x * c for x, c in d.items() if c > 1]
            unrep = [x for x, c in d.items() if c == 1]
            if sum(reps) < sum(unrep):
                ct += 1

    print(ct)
