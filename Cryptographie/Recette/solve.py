import re
import base64

# On prend la chaîne hexadécimale fournis par l'énoncé
hexa = "32 69 31 73 34 69 31 73 31 35 64 31 6f 34 39 69 31 6f 34 64 31 6f 33 69 31 6f 31 35 64 31 6f 32 32 64 31 6f 32 30 64 31 6f 31 39 69 31 6f 37 64 31 6f 35 64 31 6f 32 69 31 6f 35 35 69 31 6f 31 64 31 6f 31 39 64 31 6f 31 37 64 31 6f 31 38 64 31 6f 32 39 69 31 6f 31 32 69 31 6f 32 36 69 31 6f 38 64 31 6f 35 39 64 31 6f 32 37 69 31 6f 36 64 31 6f 31 37 69 31 6f 31 32 64 31 6f 37 64 31 6f 35 69 31 6f 31 64 31 6f 32 64 31 6f 31 32 69 31 6f 39 64 31 6f 32 36 64 31 6f"
hexa = hexa.split(" ")
print("hexa = ",hexa,"\n")

#On la converti en ASCII
decoded_hexa = ""
for elt in hexa:
    decoded_hexa += chr(int(elt, 16))
print("undeveloped deadfish = ",decoded_hexa,"\n")

#Développer de sorte à ne plus voir de chiffres
deadfish = ""
numbers = re.findall("\d+", decoded_hexa)
chars = re.findall("[a-z]", decoded_hexa)

for i in range(len(numbers)):
    deadfish += int(numbers[i])*chars[i]
print("Deadfish = ",deadfish,"\n")

#On dechiffre le dead fish avec un outil comme : https://www.dcode.fr/deadfish-language
base85_str = "1b^aR<(;4/1hgTC1NZtl1LFWKDIHFRI/"
print("Base85 = ", base85_str,"\n")

#On converti la base85 en ascii
flag = base64.a85decode(base85_str.encode())
print("Flag = ", flag)

# 404CTF{M4igr3t_D3_c4naRd}