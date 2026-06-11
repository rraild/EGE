rs = []
for x in "0123456789ABCDEF":
    n1 = int(f"D49{x}1", 16)
    n2 = int(f"48A3{x}", 16)
    tot = n1 + n2
    if tot % 14 == 0:
        rs.append(tot // 14)

print(rs[-1])
