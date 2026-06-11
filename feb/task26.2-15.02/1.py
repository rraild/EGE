with open("feb/task26.2-15.02/1.txt") as f:
    n = int(f.readline())
    day = [0] * 1441
    for s in f:
        start, end = map(int, s.split())
        for t in range(start, end + 1):
            day[t] += 1

max_visitors = max(day)

peaks_count = 0
in_peak = False

for t in range(1441):
    if day[t] == max_visitors:
        if not in_peak:
            peaks_count += 1
            in_peak = True
    else:
        in_peak = False

print(peaks_count, max_visitors)
