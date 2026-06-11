import ipaddress

net = ipaddress.ip_network("250.135.101.80/255.255.255.248", strict=False)
c = 0

for ip in net:
    bn = f"{int(ip):032b}"
    if bn.count("0") % 3 == 0:
        c += 1

print(c)
