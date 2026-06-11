import ipaddress

net = ipaddress.ip_network("211.46.0.0/255.255.128.0", strict=False)
c = 0

for ip in net:
    bn = f"{int(ip):032b}"
    if bn.count("1") % 4 == 0 and bn.endswith("11"):
        c += 1

print(c)
