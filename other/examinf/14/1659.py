def to7(num):
    res = []
    while num:
        res.append(num % 7)
        num //= 7
    return res[::-1]


n = 7**500 + 7**200 - 7**50 - 1
print((len(to7(n)) - 1) * 6)
