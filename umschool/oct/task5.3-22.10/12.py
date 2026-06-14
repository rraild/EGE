def count_ones(b):
    return b.count("1")


min_R = float("inf")

for N in range(1, 200):
    b = bin(N)[2:]
    b += b[-1]
    if count_ones(bin(N)[2:]) % 2 == 0:
        b += "0"
    else:
        b += "1"
    if count_ones(b) % 2 == 0:
        b += "0"
    else:
        b += "1"
    R = int(b, 2)
    if R > 92 and R < min_R:
        min_R = R

print(min_R)
