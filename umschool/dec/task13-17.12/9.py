from ipaddress import ip_network

ip_net = ip_network("196.168.77.128/255.255.255.0", strict=False)
print(ip_net[0])
