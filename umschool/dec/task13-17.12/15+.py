from ipaddress import ip_network

max_sum = -1
best_A, best_B = -1, -1

for A in range(256):
    for B in range(256):
        ip_net = ip_network(f"196.{A}.{B}.52/255.255.255.248", strict=False)
        t = True
        for i in ip_net:
            if not (f"{i:b}"[:16].count("0") > f"{i:b}"[-16:].count("1")):
                t = False
                break
        if t:
            if A + B > max_sum:
                max_sum = A + B
                best_A, best_B = A, B

print(max_sum)
