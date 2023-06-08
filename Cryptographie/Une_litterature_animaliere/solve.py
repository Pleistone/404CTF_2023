def decipher(cipher, key):
    b = []
    for i in range(0, len(cipher), 8):
        chunckFile = cipher[i:i+8]
        chunckKey = key[i:i+8]
        b.append(int(chunckFile, 2) ^ int(chunckKey, 2))
    return bytearray(b)

with open("chiffre.txt", "r") as f:
    chiffre = f.read()

key = "01100100011011111100010010010000001010001100011"
a = len(chiffre) // len(key)
b = len(chiffre) % len(key)
extended_key = a * key + key[:b]

image = decipher(chiffre, extended_key)

with open("flag.png", "wb") as f:
    f.write(image)