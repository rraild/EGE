import ipaddress

net = ipaddress.ip_network("115.192.0.0/255.192.0.0", strict=False)
c = 0

for ip in net:
    bn = f"{int(ip):032b}"
    if bn.count("1") % 3 != 0:
        c += 1

print(c)
