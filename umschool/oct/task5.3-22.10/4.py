def sum_digit(n):

    summ = 0

    for i in str(n):

        summ += int(i)

    return summ


R = []

for N in range(1, 10000):
    s = bin(N)[2:]

    for j in range(3):
        if sum_digit(int(s, 2)) % 2 == 0:
            s += "0"
        else:
            s += "1"

    if int(s, 2) > 522:
        R.append(int(s, 2))

print(min(R))
