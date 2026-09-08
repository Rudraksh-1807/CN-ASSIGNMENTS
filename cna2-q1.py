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
   first = int(ip.split('.')[0])

if 1 <= first <= 126:
        print("Class A")
elif 128 <= first <= 191:
        print("Class B")
elif 192 <= first <= 223:
        print("Class C")
elif 224 <= first <= 239:
        print("Class D")
elif 240 <= first <= 255:
        print("Class E")
else:
        print("Invalid Class")