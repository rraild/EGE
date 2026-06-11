max_R = 0

for N in range(1, 1000):
    binary = bin(N)[2:]
    new_binary = ""
    for digit in binary:
        if digit == "0":
            new_binary += "10"
        else:
            new_binary += "11"

    R = int(new_binary, 2)

    if R < 777 and R % 2 == 0 and R > max_R:
        max_R = R

print(max_R)
