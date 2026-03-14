import ipaddress

print("IP Addressing and Subnetting Calculator")

network = input("Enter network address (example: 192.168.10.0/24): ")

try:
    net = ipaddress.ip_network(network)

    print("\nNetwork Details")
    print("Network Address:", net.network_address)
    print("Broadcast Address:", net.broadcast_address)
    print("Total Hosts:", net.num_addresses - 2)
    print("Usable Host Range:")

    hosts = list(net.hosts())
    print("First Host:", hosts[0])
    print("Last Host:", hosts[-1])

    print("\nSubnets inside this network:")

    new_prefix = int(input("Enter new subnet prefix (example: 26): "))

    subnets = list(net.subnets(new_prefix=new_prefix))

    for i, subnet in enumerate(subnets):
        print("\nSubnet", i + 1)
        print("Network:", subnet.network_address)
        print("Broadcast:", subnet.broadcast_address)
        print("Total Hosts:", subnet.num_addresses - 2)

except:
    print("Invalid Network Address")
