for N in range(1, 2000):
    binary = bin(N)[2:]
    inv = "".join("1" if b == "0" else "0" for b in binary)
    inv_d = int(inv, 2)
    R = N - inv_d
    if R == 817:
        print(N)
        break
