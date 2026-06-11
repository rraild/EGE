def v_5(st):
    n = ""
    while st > 0:
        n += str(st % 5)
        st //= 5

    return n[::-1]


rs = []
for x in range(1, 4000):
    res = v_5(5**17 + 5**12 - x)
    if res.count("0") == 10:
        rs.append(x)

print(min(rs))
