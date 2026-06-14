import ipaddress

net = ipaddress.ip_network("10.128.0.0/255.255.192.0", strict=False)
c = 0

for ip in net:
    binary_ip = f"{int(ip):032b}"
    if binary_ip.count("1") % 4 == 0:
        c += 1

print(c)
