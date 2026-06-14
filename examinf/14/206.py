def to9(n):
    r = ""
    while n > 0:
        r += str(n % 9)
        n //= 9

    return r[::-1]


for x in range(1000):
    s = to9(81**20 - 9**x + 50)
    sm = sum(list(map(int, s)))
    if sm == 138:
        print(x)
        break
