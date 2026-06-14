import ipaddress

net = ipaddress.ip_network("235.53.0.0/255.255.224.0", strict=False)
c = 0

for ip in net:
    bn = f"{int(ip):032b}"
    if bn.count("1") % 5 == 0 and bn.endswith("110"):
        c += 1

print(c)
