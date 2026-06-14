from itertools import permutations

digits = "123456789"
count = len(list(permutations(digits, 4)))

print(count)
