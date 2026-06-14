for N in range(1, 10000):
    binary_N = bin(N)[2:]

    if N % 2 == 0:
        binary_R = binary_N + "10"
    else:
        binary_R = binary_N + "01"

    R = int(binary_R, 2)
    if R > 55:
        print(N)
        break
