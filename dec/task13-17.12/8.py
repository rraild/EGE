from ipaddress import ip_network

ip_net = ip_network("97.191.34.206/255.255.255.240", strict=False)
print(ip_net[-2])
