import ipaddress

net = ipaddress.ip_network("5.2.5.0/255.255.0.0", strict=False)
c = 0

for ip in net:
    bn = f"{int(ip):032b}"
    if bn.count("0") % 25 == 0:
        c += 1

print(c)
