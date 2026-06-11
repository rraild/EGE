import ipaddress

net = ipaddress.ip_network("90.65.32.0/255.255.224.0")
count = 0

for ip in net:
    binary_ip = f"{int(ip):032b}"
    if binary_ip.count("1") == binary_ip.count("0"):
        count += 1

print(count)
