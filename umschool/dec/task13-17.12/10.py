from ipaddress import ip_network

ip_net = ip_network("242.52.23.67/255.255.128.0", strict=False)

c = 0
for i in ip_net:
    if f"{i:b}"[16:].count("1") * 2 < f"{i:b}"[:16].count("1"):
        c += 1

print(c)
