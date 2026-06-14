import ipaddress

net = ipaddress.ip_network("172.16.192.0/255.255.192.0", strict=False)
c = 0

for ip in net:
    binary_ip = f"{int(ip):032b}"
    if binary_ip.count("1") % 5 != 0:
        c += 1

print(c)
