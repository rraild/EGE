from ipaddress import ip_network

ip_net = ip_network("167.128.120.83/255.255.255.224", strict=False)
print(ip_net[-2])
