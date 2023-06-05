# Pêche au livre

## Enoncé
Etant tranquillement assis au café littéraire, vous entendez Albert Camus discuter avec quelqu'un d'autre.

Vous comprenez qu'après avoir écrit son dernier livre, il s'interroge sur l'actualité du monde littéraire. Il fait donc des recherches sur ses homologues écrivains et plus particulièrement sur Simone Weil, dont il a beaucoup entendu parlé ces derniers jours, et se demande quel sera le sujet de son prochain livre...

Justement, vous avez récemment intercepté des communications de Simone Weil, peut être pourrez vous trouver le sujet de son prochain ouvrage.


## Solution

Le fichier fourni est une capture réseau, on commence par l'analyser avec le logiciel Wireshark : 

<p align="center"><img src="Echange HTTP.png" alt="Echange HTTP" width="500"></p>

On constate qu'il s'agit d'un échange HTTP qui a été capturé.
Ce dernier n'est donc pas chiffré, on extraire le contenu de cet échange, en allant dans le menu `Fichier > Exporter Objets > HTTP`.
Cette opération permet de récupérer trois images, dont l'une d'entre elles contient le flag.

<details>
<summary> Flag 🚩</summary>
```404CTF{345Y_W1r35h4rK}```

<p align="center"><img src="./HTTP files/Hegel-sensei-uwu.png" alt="Flag" width="200"></p>

