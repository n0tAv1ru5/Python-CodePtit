import ipaddress

for _ in range(int(input())):
    try:
        ip = ipaddress.IPv4Address(input())
        print("YES")
    except ipaddress.AddressValueError:
        print("NO")
