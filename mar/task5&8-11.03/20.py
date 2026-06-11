from itertools import product

cnt = 0
digits = range(21)
big_digits = set(range(12, 21))

for w in product(digits, repeat=6):
    if w[0] != 0:
        if w.count(6) == 1:
            big_cnt = 0
            for d in w:
                if d in big_digits:
                    big_cnt += 1

            if big_cnt >= 3:
                cnt += 1

print(cnt)
