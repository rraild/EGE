from ipaddress import ip_network

ip_net = ip_network("176.54.23.0/255.255.192.0", strict=False)

c = 0
for i in ip_net:
    if f"{i:b}".count("1") % 3 == 0:
        c += 1

print(c)
