f = open("1.txt")

s = f.readline()

max_k = 0

k = 1

for i in range(len(s) - 1):

    if s[i] != s[i + 1]:

        k += 1

        max_k = max(max_k, k)

    else:

        k = 1

print(max_k)
