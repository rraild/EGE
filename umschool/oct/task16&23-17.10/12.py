# import sys

# sys.setrecursionlimit(100000)


# def F(m, n):
#     if m == 0:
#         return n + 1
#     elif n == 0:
#         return F(m - 1, 1)
#     else:
#         return F(m - 1, F(m, n - 1))


# print(F(4, 1))
F = []

for i in range(10):

    F.append([0] * 1000000)

for m in range(10):

    for n in range(500000):

        if m == 0:

            F[m][n] = n + 1

        if m > 0 and n == 0:

            F[m][n] = F[m - 1][1]

        if m > 0 and n > 0:

            F[m][n] = F[m - 1][F[m][n - 1]]

print(F[4][1])
