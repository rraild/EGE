import ipaddress

net = ipaddress.ip_network("172.140.68.0/255.255.248.0", strict=False)
c = 0

for ip in net:
    bn = f"{int(ip):032b}"
    if bn.count("0") > 15:
        c += 1

print(c)
