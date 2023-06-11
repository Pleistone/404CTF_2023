# Le Rouge et le vert, avec un soupçon de bleu

**Difficulté** : Difficile

## Enoncé

Ce qui semble être un brouillon a été laissé sur une table en hâte par un jeune homme. Vous vous rapprochez pour le lui rendre, mais il a déjà disparu. Vous décidez de lire ce bout de papier pour déterminer la personnalité de son auteur. Le début ressemble à un poème. La fin quant à elle a l'air assez spéciale...

Toutes les informations nécessaires à la résolution de ce challenge sont présentes dans l'énoncé ci-dessus. Déchiffrez la fin du poème.


## Solution

Dans l'énoncé, on nous indique qu'à la fin du document il y avait quelque chose d'assez spécial. À la fin de l'image, on peut clairement voir le message codé, mais il manque des morceaux.

<p align="center"><img src="Message code.png" alt="Message code" width="500"></p>

Ces morceaux manquants sont masqués par des bandes de couleur (rouge, bleu, vert et blanc). Il est donc nécessaire de déterminer les chiffres cachés derrière chaque bande de couleur afin de reconstituer le message. Pour le moment, on recopie les chiffres connus et pour les chiffres inconnus, on utilise les caractères "W" pour ceux cachés derrière du blanc, "R" pour le rouge, "G" pour le vert et "B" pour le bleu. Ainsi, on obtient :  
`76WWW321021089710332WWW115116581089795118RRRWWW95WWW1109599BBBGGG108WWWGGG114115125`

Comme on ne sait pas trop de quoi il peut s'agit, même si on a quelques hypothèses, on l'envoie sur [dCode - Indentifier](https://www.dcode.fr/identification-chiffrement) qui nous trouve un résultat intéressant : de l'ASCII. On utilise donc [dCode - ASCII](https://www.dcode.fr/code-ascii) pour déchiffrer le tout :

<p align="center"><img src="Code ascii.png" alt="Décode ascii" width="500"></p>

À partir des parties déjà déchiffrées `L* flag *st:la_v**_*n_c**l**rs}`, on peut faire les hypothèses suivantes :  
- Dériree WWW on à un e donc 101
- Dériree RRR on à un i donc 105
- Dériree GGG on à un o donc 111
- Dériree BBB on à un u donc 117

Ce qui nous donne le message suivant :
`Le flag est:la_vie_en_couleurs}`


## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{la_vie_en_couleurs}
```


