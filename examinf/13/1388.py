import ipaddress

net = ipaddress.ip_network("11.92.135.56/255.224.0.0", strict=False)

max_ip = net.broadcast_address - 1

octets = str(max_ip).split(".")
print("".join(octets))
