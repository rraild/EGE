import ipaddress

net = ipaddress.ip_network("192.168.32.160/255.255.255.240", strict=False)
count = 0

for ip in net:
    binary_ip = f"{int(ip):032b}"
    if binary_ip.count("0") > 21:
        count += 1

print(count)
