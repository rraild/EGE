import ipaddress

net = ipaddress.ip_network("167.66.136.176/255.254.0.0", strict=False)

ls = list(net.hosts())
min_ip = sorted(ls)[-1]
print(min_ip)
print(167 + 67 + 255 + 254)
