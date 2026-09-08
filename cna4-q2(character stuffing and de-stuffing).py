def character_stuffing(data):
    flag = 'F'
    escape = 'E'

    stuffed = flag

    for ch in data:
        if ch == flag or ch == escape:
            stuffed += escape

        stuffed += ch

    stuffed += flag

    return stuffed


def character_destuffing(data):
    flag = 'F'
    escape = 'E'

    
    data = data[1:-1]

    destuffed = ""
    i = 0

    while i < len(data):
        if data[i] == escape:
            i += 1

        destuffed += data[i]
        i += 1

    return destuffed



data = input("Enter the data: ")

stuffed_data = character_stuffing(data)
print("After Character Stuffing   :", stuffed_data)

destuffed_data = character_destuffing(stuffed_data)
print("After Character Destuffing :", destuffed_data)