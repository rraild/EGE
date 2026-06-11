from ipaddress import ip_network

ip_net = ip_network("252.32.33.87/255.255.0.0", strict=False)

c = 0
for i in ip_net:
    if f"{i:b}"[-16:].count("1") > f"{i:b}"[:16].count("1") * 2:
        c += 1

print(c)
