c = 0
for n in range(600_001, 600_001 + 100):
    for i in range(17, n, 10):
        if n % i == 0:
            print(n, i)
            c += 1
            break

    if c == 5:
        break
