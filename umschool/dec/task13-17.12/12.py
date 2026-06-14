from ipaddress import ip_network

c = 0
for A in range(256):
    ip_net = ip_network(f"207.0.{A}.163/255.255.255.192", strict=False)
    for i in ip_net:
        if not (f"{i:b}"[:16].count("0") > f"{i:b}"[-16:].count("0")):
            break

    else:
        c += 1
print(c)
