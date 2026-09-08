ip = input("Enter IP address: ")

first = int(ip.split('.')[0])

if 1 <= first <= 126:
    print("Default Subnet Mask: 255.0.0.0")
elif 128 <= first <= 191:
    print("Default Subnet Mask: 255.255.0.0")
elif 192 <= first <= 223:
    print("Default Subnet Mask: 255.255.255.0")
elif 224 <= first <= 239:
    print("Class D: No default subnet mask")
elif 240 <= first <= 255:
    print("Class E: No default subnet mask")
else:
    print("Invalid IP address")