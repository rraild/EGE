with open("other/examinf/17/1197.txt") as f:
    c = 0
    mx = 0
    f = f.read().split()
    kall_okocnh7 = len([int(x) for x in f if abs(int(x)) % 10 == 7])
    print(kall_okocnh7)
    for i in range(len(f) - 1):
        a, b = int(f[i]), int(f[i + 1])
        if (a * b) < 0:
            if a + b < kall_okocnh7:
                mx = max((a + b), mx)
                c += 1

print(c, mx)
