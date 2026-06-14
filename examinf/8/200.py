from itertools import product

abc = sorted("ПРИВЫЧКА")
cons = set("ПРВЧК")

new_i = 0
old_i = 0

for w in product(abc, repeat=5):
    old_i += 1
    if old_i % 5 == 0:
        continue
    new_i += 1
    if all(c in cons for c in w) and len(set(w)) == 5:
        print(new_i)
        break
