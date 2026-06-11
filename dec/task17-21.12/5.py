# Определите количество пар , сумма квадратов которых четна и больше 80,
# а также максимальный элемент такой пары, при условии,
# что сумма её элементов минимальна.
# сначала количество, затем максимальное значение.

with open("dec/task17-21.12/5.txt") as f:
    c = 0
    mx = -1
    mn = 10**9
    data = [int(x) for x in f.readlines()]

    for i in range(len(data) - 1):
        if (data[i] + data[i + 1]) % 2 == 0 and (
            data[i] ** 2 + data[i + 1] ** 2
        ) > 80:
            c += 1
            pair_sum = data[i] + data[i + 1]
            if pair_sum < mn:
                mn = pair_sum
                mx = max(data[i], data[i + 1])

    print(c, mx)
