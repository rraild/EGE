from ipaddress import ip_network

ip_net = ip_network("213.232.128.145/255.255.128.0", strict=False)

c = 0
for i in ip_net:
    if f"{i:b}".count("0") % 5 == 0:
        c += 1

print(c)
