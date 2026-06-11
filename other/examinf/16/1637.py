# def F(n):
#     if n >=57000:
#         return F(n-2) + 3552 + F(n-3)

#     return 222 + G(n-2) + G(n-1)


# def G(n):
#     if n >= 9999:
#         return G(n-5) + G(n-3) + 157

#     return 15 * (2*n+4)

# print((F(2540)))
# print(1*5*2*6*5*2)
from math import prod

a = 152652
print(prod(list(map(int, str(a)))))
