third_byte = 65
mask = 224
zeros_third = bin(third_byte).count("0")

count = 0
for A in range(256):
    network_base = A & mask
    if all(
        zeros_third > bin(i).count("0")
        for i in range(network_base + 1, network_base + 31)
    ):
        count += 1

print(count)
