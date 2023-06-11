# Avez-vous vu les cascades du hérisson ?

**Difficulté** : Facile

## Enoncé

Après avoir rencontré Simone, cette dernière vous propose de découvrir une nouvelle personne. Quoi de mieux qu’un cache-cache pour apprendre à mieux se connaître ? Cela vous changera de l'air du café littéraire Le Procope.

Vous arrivez dans un lieu qui lui est cher, un lieu d’enfance rempli de souvenirs. C’est ici qu’elle passait ces vacances d’Été, dans le parc de Meyrignac, fondé en 1880 par son grand père Ernest BERTRAND DE BEAUVOIR.

Lors de votre partie, non loin de là, vous parvenez habilement à trouver Simone, cependant le troisième joueur demeure parfaitement introuvable. Votre cerveau titanesque a eu la bonne idée de faire ce jeu dehors, en pleine nature, pour plus de difficulté. Sublime. Vous voilà errant au milieu de nulle part. Toutefois, un bruit vous attire :

« SPLASHHHH... SHHHHH... SPLASHHHH... SHHHHH... » (Le son d'une cascade d'eau qui tombe et qui ruisselle)

Cette chute d'eau paraît ordinaire et suspicieuse. Peut-être parviendrez-vous à trouver ce charmant flibustier à travers les cascades du Hérisson avant qu'il soit l'heure de rentrer au Procope ?

Vous avez un oeil de lynx, ainsi vous apercevez que la chute d'eau s'écoule à une fréquence de 2 MHz

> Format du flag : 404CTF{ceci_est_un_flag}


## Solution

Le principe du challenge est de regarder le spectrogramme du signal, ou waterfall en anglais. C'est une représentation temps-fréquence en 3D, où apparaissent le temps, la fréquence et la répartition d'énergie. On ouvre le fichier .raw sur Audacity en allant dans le menu `Fichier > Importer > Données brutes (.raw)`. Avant de valider l'importation, nous cliquons sur "Detect" pour obtenir les meilleurs paramètres d'importation.

Une fois le fichier ouvert, nous affichons le spectrogramme et on applique un "zoom adapté", on obtient alors l'image suivante :

<p align="center"><img src="Audacity spectrogramme.png" alt="Audacity spectrogramme" width="900"></p>

On voit bien que l'on est sur la bonne piste, mais le texte n'est pas tout à fait visible. On va donc modifier les paramètres du spectrogramme : 

<p align="center"><img src="Spectrogramme ajuste.png" alt="Spectrogramme ajusté" width="900"></p>

On prend une capture d'écran du spectrogramme et on l'édite un peu pour rendre le tout un peu plus lisible : 

<p align="center"><img src="Image editer.png" alt="Image editer" width="500"></p>


## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{413x4ndR3_d4n5_Un3_C45c4d35_?}
```
