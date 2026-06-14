from itertools import combinations

digits = "01234"
count = 0

for p in combinations(digits, 4):
    count += 1

print(count)
