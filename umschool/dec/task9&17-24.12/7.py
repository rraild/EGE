# Определите количество троек элементов последовательности, в которых только
# один из трех элементов является четырехзначным, а сумма элементов тройки
# не больше максимального элемента последовательности, делящегося на 14.
# В ответе запишите количество найденных троек, а затем максимальную
# из сумм элементов таких троек.

with open("dec/task9&17-24.12/7.txt") as f:
    ct = 0
    mx_sum = 0
    d = [int(x) for x in f.readlines()]
    for i in range(len(d) - 2):
        triple = [d[i], d[i + 1], d[i + 2]]
        four_digit_count = sum(1 for x in triple if 1000 <= x <= 9999)
        max_div_14 = max((x for x in d if x % 14 == 0), default=0)

        if four_digit_count == 1 and sum(triple) <= max_div_14:
            ct += 1
            mx_sum = max(mx_sum, sum(triple))

    print(ct, mx_sum)
