# Un courrier suspect

## Enoncé

Vous commencez à profiter de la vue offerte par ce café pittoresque ainsi que de vos premières gorgées de café quand vous sentez une présence derrière vous.   
« Bienvenue, novice. Moi c'est Jean Paul Sartre, mais on m'appelle plutôt Jean Paul Sat par ici. »   
À peine avez vous eu le temps de vous retourner, que cet individu vous met dans les mains une platine sur laquelle figure un circuit. Il vous tend également une petite feuille, qui parle d'un "test de remise à niveau".   
« Et voici les instructions. »

Il vous regarde avec insistance.

## Solution

Le challenge nous fournit un fichier nommé bienvenue.circ. Après quelques recherches, on découvre que l'on peut ouvrir ce type de fichier avec le logiciel Logisim. On ouvre donc le fichier et on constate qu'il est composé de plusieurs parties. On commence par la partie 1, où l'on trouve le début du flag :

<p align="center"><img src="Partie 1.png" alt="Partie 1" width="500"></p>

En passant à la partie 2, on nous indique d'utiliser l'outil en forme de main pour cliquer sur l'horloge du circuit, ce qui va avoir pour effet d'exécuter le programme et d'afficher une suite de nombres hexadécimaux sur l'afficheur. On obtient alors la séquence suivante : 4d 30 6d 33 6e 54 5f 33 53 74 5f 56 33 6e 55 5f

<p align="center"><img src="Partie 2.png" alt="Partie 2" width="700"></p>

Dans la partie 3, on nous explique qu'on peut utiliser l'outil curseur pour éditer les valeurs en input. On va donc utiliser cet outil pour mettre en entrée la chaîne hexadécimale que l'on a trouvée précédemment. On obtient ainsi un autre morceau du flag.

<p align="center"><img src="Partie 3.png" alt="Partie 3" width="700"></p>

Dans la partie 4, on nous explique qu'on peut modifier le circuit à l'aide du curseur. On remarque qu'on a affaire à un circuit similaire à celui de l'étape 2, mais qui ne semble pas fonctionner lorsque l'on active l'horloge. On constate alors la présence d'une blackbox qui bloque le signal vers l'afficheur. On la supprime donc et on connecte les câbles. Ça fonctionne ! On peut alors récupérer une nouvelle chaîne hexadécimale : 00 00 00 00 00 44 33 5f 35 34 6d 75 73 33 72 7d, que l'on met en entrée de la partie 3. On obtient ainsi la fin du flag.

<p align="center"><img src="Partie 4.png" alt="Partie 4" width="500"></p>

## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{L3_M0m3nT_3St_V3nU_D3_54mus3r}
```