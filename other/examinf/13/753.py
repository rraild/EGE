import ipaddress

net = ipaddress.ip_network("214.187.224.0/255.255.224.0", strict=False)
c = 0

for ip in net:
    binary_ip = f"{int(ip):032b}"
    if binary_ip.count("1") % 6 != 0 and binary_ip.endswith("1000"):
        c += 1

print(c)
