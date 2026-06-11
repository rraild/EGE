# Определите количество пар из которых хотя бы одно число – это квадрат
# натурального числа, а также максимальную сумму элементов таких пар.
# сначала количество, затем максимальное значение.

with open("dec/task17-21.12/4.txt") as f:
    c = 0
    mx = -1
    d = [int(x) for x in f.readlines()]

    def is_square(n):
        if n < 0:
            return False
        root = int(n**0.5)
        return root * root == n

    for i in range(len(d) - 1):
        if is_square(d[i]) or is_square(d[i + 1]):
            c += 1
            mx = max(mx, d[i] + d[i + 1])

    print(c, mx)
