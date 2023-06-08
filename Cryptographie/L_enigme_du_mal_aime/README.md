# Le Jour de l'espace

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

On renomme donc notre fichier chiffre.png en chiffre.txt, puis on l'ouvre avec un éditeur de texte. On voit que le texte est constitué d'uniquement des 1 et des 0. On a un total de 29 740 656 caractères, qui comme par hasard est un multiple de 8. Il est donc clair que nous devons regrouper les bits de ce fichier texte en octets. 

Etant donner que l'on est dans un challenge crypto, le fichier a certainement dû être chiffré. On se demande alors quel chiffrement, assez simple pour que le chall soit classé facile, renvoie directement une série de bits ? Probablement un XOR. Le problème du XOR, c'est qu'il faut une partie du message en clair. C'est la que l'on peut si dire que finalement chiffre.png est bien un PNG mais un PNG chiffré.


<p align="center"><img src="flag.png" alt="Le flag" width="500"></p>

## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{1g0rfu4v3rt1Env4ut2}
```

