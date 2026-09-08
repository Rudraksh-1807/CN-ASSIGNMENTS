def validate_ip(ip):
    
    for ch in ip:
        if not (ch.isdigit() or ch == '.'):
            return False

    
    if ip.count('.') != 3:
        return False

    parts = ip.split('.')

    if len(parts) != 4:
        return False

    for part in parts:
        if part == "":
            return False

        
        if len(part) > 1 and part[0] == '0':
            return False

        num = int(part)

        
        if num < 0 or num > 255:
            return False

    return True


ip = input("Enter IP Address: ")

if not validate_ip(ip):
    print("Invalid IP Address")
else:
    parts = ip.split('.')

    print("32-bit Binary Address:")
    binary = ""

    for i in range(4):
        binary += format(int(parts[i]), '08b')
        if i != 3:
            binary += "."

    print(binary)