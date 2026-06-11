from itertools import combinations, permutations

even_digits = [0, 2, 4, 6, 8, 10]
odd_digits = [1, 3, 5, 7, 9, 11]

total_count = 0

for odds in combinations(odd_digits, 4):
    for evens in combinations(even_digits, 5):
        all_digits = list(odds) + list(evens)
        for p in permutations(all_digits):
            if p[0] != 0 and p[-1] % 2 != 0:
                total_count += 1

print(total_count)
