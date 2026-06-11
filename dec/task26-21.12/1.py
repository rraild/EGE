with open("dec/task26-21.12/1.txt") as f:
    k = int(f.readline())
    n = int(f.readline())

    c, ls_disk = 0, 0
    files = []

    for s in f:
        start, end = map(int, s.split())
        files.append([start, end])

    files.sort()
    disks = [0] * k

    for start, end in files:
        for i in range(k):
            if start > disks[i]:
                disks[i] = end
                c += 1

                ls_disk = i + 1
                break

    print(c, ls_disk)
