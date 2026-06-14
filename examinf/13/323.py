import ipaddress

net1 = ipaddress.ip_network("192.168.56.192/255.255.255.192", strict=False)
net2 = ipaddress.ip_network("192.168.56.208/255.255.255.240", strict=False)

set1 = set(net1)
set2 = set(net2)

r = set1 ^ set2
print(len(r))
