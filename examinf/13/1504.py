import ipaddress

net = ipaddress.ip_network("111.194.0.0/255.254.0.0")
c = 0

for ip in net:
    if ip == net.network_address or ip == net.broadcast_address:
        continue

    bn = f"{int(ip):032b}"
    c1 = bn.count("1")
    c0 = bn.count("0")

    if (c1 - c0) % 2 == 0:
        c += 1

print(c)
