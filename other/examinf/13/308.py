import ipaddress

ip1 = ipaddress.ip_address("211.188.211.49")
ip2 = ipaddress.ip_address("211.188.200.115")

mx = 0
for ln in range(32, -1, -1):
    net1 = ipaddress.ip_network(f"{ip1}/{ln}", strict=False)
    net2 = ipaddress.ip_network(f"{ip2}/{ln}", strict=False)
    if net1 == net2:
        mx = ln
        break

f = ipaddress.ip_network(f"{ip1}/{mx}", strict=False)
c = 0
for ip in f:
    if bin(int(ip)).count("1") % 2 != 0:
        c += 1

print(c)
