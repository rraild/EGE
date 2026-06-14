def to3(n):
    s = ""
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]


for x in range(1, 2031):
    val = 3**100 - x
    if to3(val).count("0") == 1:
        print(x)
