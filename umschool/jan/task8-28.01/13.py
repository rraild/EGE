from itertools import product

letters = "ЗАРЯ"
count = 0

for p in product(letters, repeat=5):
    word = "".join(p)

    count_r = word.count("Р")
    if count_r > 1:
        continue

    if count_r == 1:
        if word[0] == "Р" or word[-1] == "Р":
            continue

        if "РЯ" in word or "ЯР" in word:
            continue

    count += 1

print(count)
