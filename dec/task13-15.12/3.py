from ipaddress import ip_network

ip_net = ip_network("142.96.56.118/255.255.255.240", strict=False)

c = 0
for i in ip_net:
    if f"{i:b}"[-16:].count("1") > f"{i:b}"[:16].count("1"):
        c += 1

print(c)
