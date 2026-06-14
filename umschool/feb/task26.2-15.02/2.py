with open("feb/task26.2-15.02/2.txt") as f:
    n = int(f.readline())

    time_start, time_end = 8 * 60 * 60, 14 * 60 * 60
    process = [0] * 86401

    for i in range(n):
        start, end = map(int, f.readline().split())
        process[start] += 1
        process[end] -= 1

    current_process = max_process = max_length = 0

    for second in range(len(process)):
        current_process += process[second]
        if time_start <= second <= time_end:
            if current_process > max_process:
                max_process = current_process
                max_length = 1

            elif current_process == max_process:
                max_length += 1

print(max_process, max_length)
