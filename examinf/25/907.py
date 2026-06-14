import fnmatch

mask = "112?57*4"
for s in range(2024, 10**10, 2024):
    sm = sum(list(map(int, str(s))))
    if s % 2024 == 0:
        if sm % 2 != 0:
            if fnmatch.fnmatch(str(s), mask):
                print(s, s // 2024)
