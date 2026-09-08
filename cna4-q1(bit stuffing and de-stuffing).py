def bit_stuffing(data):
    stuffed = ""
    count = 0

    for bit in data:
        stuffed += bit

        if bit == '1':
            count += 1
            if count == 5:
                stuffed += '0'
                count = 0
        else:
            count = 0

    return stuffed


def bit_destuffing(data):
    destuffed = ""
    count = 0
    i = 0

    while i < len(data):
        destuffed += data[i]

        if data[i] == '1':
            count += 1

            if count == 5:
                
                if i + 1 < len(data) and data[i + 1] == '0':
                    i += 1
                count = 0
        else:
            count = 0

        i += 1

    return destuffed



data = input("Enter the binary data: ")

stuffed_data = bit_stuffing(data)
print("After Bit Stuffing :", stuffed_data)

destuffed_data = bit_destuffing(stuffed_data)
print("After Bit Destuffing:", destuffed_data)