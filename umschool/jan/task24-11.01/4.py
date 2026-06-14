def sum_digits(n):
    s = 0
    for i in str(n):
        s += int(i) ** len(str(n))

    return s


f = open("jan/task24-11.01/4.txt")
s = f.readline()
max_number = 0
for i in range(len(s) - 5):
    for j in range(1, 5 + 1):
        k = int(s[i : i + j])
        if k == sum_digits(k):
            max_number = max(max_number, k)

print(s.count(str(max_number)))
