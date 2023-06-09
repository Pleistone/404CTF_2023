# Une littérature animalière

**Difficulté** : Facile

## Enoncé

Au café littéraire, vous bavardez avec Voltaire. Il se trouve que ce petit sacripan s'est infiltré dans la maison de Rousseau pour trouver des informations compromettantes sur son nouveau livre "Le Gorfou ou de l'éducation". La seule chose qu'il a récupéré est un étrange fichier, qu'il a mis dans son manteau avant de prendre la poudre d'escampette. Il espère pouvoir obtenir votre aide pour lire ce fichier décidément bien étrange...

Bonne chance

## Solution

Dans ce challenge, nous avons à disposition un fichier chiffre.wav dans lequel est caché un flag.
En essayant d'ouvrir le fichier tel, on peut voir que le fichier ne s'ouvre pas correctement. Il pourrait s'agir d'un autre type de fichier.
```
file chiffre.wav
> chiffre.wav: Zip archive data, at least v2.0 to extract, compression method=deflate
```

On renomme donc notre fichier chiffre.wav en chiffre.zip, puis on le décompresse. En l'ouvrant, on obtient un dossier avec une image chiffre.png. Malheureusement, cette image a aussi des problèmes pour s'ouvrir.
```
file chiffre.png
> chiffre.png: ASCII text, with very long lines (65512), with no line terminators
```

On renomme donc notre fichier chiffre.png en chiffre.txt, puis on l'ouvre avec un éditeur de texte. On voit que le texte est constitué uniquement de 0 et de 1. On a un total de 29 740 656 caractères, qui, comme par hasard est un multiple de 8. Il est donc clair que nous devons regrouper les bits de ce fichier texte en octets. 

Étant donné que nous sommes confrontés à un défi de cryptographie, il est probable que le fichier ait été chiffré. On se demande alors quel chiffrement, suffisamment simple pour que le défi soit classé comme facile, renvoie directement une séquence de bits. Il est fort probable qu'il s'agisse d'un chiffrement XOR. Le problème du XOR, c'est qu'il faut une partie du message en clair pour le déchiffrer. C'est à ce moment-là que l'on réalise que le fichier chiffre.png est effectivement un PNG, mais un PNG chiffré.

Or le [header d'un PNG](https://fr.wikipedia.org/wiki/Portable_Network_Graphics#Signature_PNG) commencent toujours par les mêmes 8 premiers octets.
On récupère les 8 octets (64 bits) de la signature d'un PNG et on fait un XOR avec les 64 premiers bits de notre fichier.
```python
with open("chiffre.png", "r") as f:
    chiffre = f.read()

chiffre = chiffre[0:64]
png_sig = [137, 80, 78, 71, 13, 10, 26, 10]
res = ""

for i in range(0, len(chiffre), 8):
    byte = chiffre[i:i+8]
    xor = int(byte, 2) ^ png_sig[i//8]
    res += "{0:0>8b}".format(xor) # Convert int to bit string

print(res) 
```

On obtient alors la suite de bit si dessous, dans laquelle est cachée la (très probable) clé
```
0110010001101111110001001001000000101000110001101100100011011111
```

En effet, on voit que la série se répète à partir du 48ème caractères, visible si on écrit la suite sur deux lignes
```
01100100011011111100010010010000001010001100011   
01100100011011111
```

On a donc trouvé la clé de chiffrement qui va nous permettre de déchiffrer le fichier.
```python
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
```

Et voilà ! On obtient une belle image après déchiffrement.

<p align="center"><img src="flag.png" alt="Le flag" width="500"></p>

## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{1g0rfu4v3rt1Env4ut2}
```

