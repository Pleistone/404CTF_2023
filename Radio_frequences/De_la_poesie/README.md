# Navi

**Difficulté** : Introduction

## Enoncé

En vous installant à une table, sirotant tranquillement une boisson, vous entendez le bruit monter à l’intérieur du café littéraire.

C'est à ce moment qu'une femme vient s'assoir en face de vous. Elle se présente comme étant **Simone DE BEAUVOIR**. Vous vous étiez déjà rencontrés lors des comités de lecture des éditions Gallimard.

Pendant votre discussion absolument passionnante, la radio du café diffuse une lecture de La ruelle des lutins. C'est à ce moment que son auteur, **Alexandre DUMAS**, vient se joindre à votre compagnie.

Toutefois, vous remarquez que ce dernier semble intrigué par la narration, pensant qu'elle doit cacher quelque chose...

Le fichier est au format .raw, correspondant à des données brutes — on peut également avoir des fichiers sans extension. Ces fichiers peuvent être lus dans des logiciels comme GNU-Radio (un SDR) ou Audacity (ce dernier est plus simple d'utilisation). Port du casque conseillé.


## Solution

On ouvre le fichier .raw sur Audacity en allant dans le menu `Fichier > Importer > Données brutes (.raw)`. Une fois le fichier importé, on augmente la vitesse de lecture de 4.5 fois et on inverse le sens de lecture. Vers la fin de l'audio, une voix nous donne le message suivant : "la solution est en hexadécimal 34 30 34 43 54 46 7b 31 74 72 30 5f 34 55 78 5f 52 34 64 31 30 2d 66 52 33 71 55 33 4e 63 33 35 7d". Nous déchiffrons ensuite ce message hexadécimal pour obtenir le flag.


## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{1tr0_4Ux_R4d10-fR3qU3Nc35}
```
