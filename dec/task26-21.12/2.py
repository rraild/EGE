with open("dec/task26-21.12/2.txt") as f:
    n = int(f.readline())
    start = []
    end = []
    for i in range(n):
        slif, okr = map(int, f.readline().split())
        if slif < okr:
            start.append([slif, i + 1])

        else:
            end.append([okr, i + 1])

start.sort()
end.sort()
print(max(start), max(end))
print(len(start) - 1)
# 809 530
