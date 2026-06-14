from ipaddress import ip_network

ip_net = ip_network("231.168.192.196/255.255.255.240", strict=False)

c = 0
for i in ip_net:
    if f"{i:b}".count("1") % 2 != 0:
        print(i)
        c += 1

print(c)
