import ipaddress

net = ipaddress.ip_network("143.168.72.213/255.255.255.224", strict=False)

print(net.broadcast_address - 1)
