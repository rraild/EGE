from itertools import product

cnt = 0
i = 0

for w in product(sorted("ТБДЦЭЕКНЧ"), repeat=6):
    i += 1
    if i % 2 == 0 and w[0] != "Н" and w[-1] != "Н" and w.count("Е") >= 3:
        cnt += 1

print(cnt)
