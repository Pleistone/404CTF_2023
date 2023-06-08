# Recette

## Enoncé

Le Commissaire Maigret, café à la main, vous raconte une de ses dernières enquêtes. Il vous explique que sur une scène de crime il a retrouvé un papier faisant office de message codé. Il le sort de sa poche pour vous le montrer :

Convertir depuis l'hexadécimal   
Développer de sorte à ne plus voir de chiffres   
Décoder le DeadFish   
Convertir depuis la Base 85   

Suivi de la séquence : 32 69 31 73 34 69 31 73 31 35 64 31 6f 34 39 69 31 6f 34 64 31 6f 33 69 31 6f 31 35 64 31 6f 32 32 64 31 6f 32 30 64 31 6f 31 39 69 31 6f 37 64 31 6f 35 64 31 6f 32 69 31 6f 35 35 69 31 6f 31 64 31 6f 31 39 64 31 6f 31 37 64 31 6f 31 38 64 31 6f 32 39 69 31 6f 31 32 69 31 6f 32 36 69 31 6f 38 64 31 6f 35 39 64 31 6f 32 37 69 31 6f 36 64 31 6f 31 37 69 31 6f 31 32 64 31 6f 37 64 31 6f 35 69 31 6f 31 64 31 6f 32 64 31 6f 31 32 69 31 6f 39 64 31 6f 32 36 64 31 6f

## Solution

Pour résoudre ce challenge, il suffit d'appliquer, sur la séquence fournis, les instructions fournis les unes après les autres. Pour faire cela, on peut faire un code python comme on trouve dans solve.py où utiliser un logiciel comme [Cyberchef](https://cyberchef.org/).

1. Première étape, on converti la chaîne hexadécimale en ASCII
```
2i1s4i1s15d1o49i1o4d1o3i1o15d1o22d1o20d1o19i1o7d1o5d1o2i1o55i1o1d1o19d1o17d1o18d1o29i1o12i1o26i1o8d1o59d1o27i1o6d1o17i1o12d1o7d1o5i1o1d1o2d1o12i1o9d1o26d1o
```

2. On développe cette chaîne de caractère pour qu'il ne reste que des chiffres.
```
iisiiiisdddddddddddddddoiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiioddddoiiiodddddddddddddddoddddddddddddddddddddddoddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiodddddddodddddoiioiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiododddddddddddddddddddodddddddddddddddddoddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiiiiiiiiiioiiiiiiiiiiiioiiiiiiiiiiiiiiiiiiiiiiiiiioddddddddodddddddddddddddddddddddddddddddddddddddddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiiiiiiiioddddddoiiiiiiiiiiiiiiiiioddddddddddddodddddddoiiiiiododdoiiiiiiiiiiiiodddddddddoddddddddddddddddddddddddddo
```

3. On déchiffre le deadfish.
```
1b^aR<(;4/1hgTC1NZtl1LFWKDIHFRI/
```

4. On converti la base85 en ascii et on trouve le flag.


## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{M4igr3t_D3_c4naRd}
```