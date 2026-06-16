import fnmatch

mask = "21*93?3*5?2"

for s in range(2026, 10**10, 2026):
    if fnmatch.fnmatch(str(s), mask):
        print(s, s // 2026)
