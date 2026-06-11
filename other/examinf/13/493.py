import ipaddress

net = ipaddress.ip_network("112.160.0.0/255.240.0.0", strict=False)
c = 0

for ip in net:
    if bin(int(ip)).count("1") % 5 == 0:
        c += 1

print(c)
