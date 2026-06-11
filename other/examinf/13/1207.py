import ipaddress

net = ipaddress.ip_network("222.121.128.0/255.255.224.0", strict=False)
c = 0

for ip in net:
    binary_ip = f"{int(ip):032b}"
    if binary_ip[-1] == binary_ip[-2]:
        c += 1

print(c)
