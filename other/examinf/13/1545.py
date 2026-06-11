import ipaddress

net = ipaddress.ip_network("95.24.30.144/255.255.248.0", strict=False)

ls = list(net.hosts())
min_ip = min(ls)

octets = [int(x) for x in str(min_ip).split(".")]
print(sum(octets))
