# La Quête du sens [2/3]

**Difficulté** : Moyen

## Enoncé

Vous vous rappelez de son nom maintenant. Marceline Desbordes-Valmore, passionnée d'écriture et de musique ! Elle est connue au salon pour ses inventions aussi imprévisibles qu'éphémères. Elle se penche soudainement d'un air enjoué vers vous. Vous n'avez pas le temps d'essayer d'esquiver le long monologue qui s'annonce qu'elle est déjà lancée sur sa dernière idée : publier un journal dont les auteurs seraient des écrivains romantiques ! Vous lui faites remarquer que ce concept n'est peut-être pas si original que cela. Vexée, elle pianote furieusement sur son téléphone, bien décidée à vous montrer que vous avez tort. Elle tombe alors sur un étrange échange de message dans un forum obscur :

Sainte-Marie : Je crois que notre journal n'a pas beaucoup de succès.   
Auverney : Pourtant, qui n'a pas besoin d'un peu de romantisme dans sa vie ?   
Sainte-Marie : il faut se rendre à l'évidence, nous allons devoir arrêter cette activité.   
Auverney : ... il est dur de se faire une raison, mais j'accepte. On en parle aux autres d'abord ? @Frères ?   
Marceline, embêtée de ne pas avoir eu l'idée en premier, veut à tout prix retrouver le nom de ce journal impopulaire. Saurez-vous le lui fournir ?   

> Format : 404CTF{nom_du_journal}


## Solution

En effectuant une lecture attentive de l'énoncé, on parvient à déterminer différents critères pour le journal recherché. On est à la recherche d'un journal datant de l'époque romantique, soit entre 1800 et 1850. Ce journal n'a pas été publié pendant une longue période. De plus, il est rédigé par des auteurs romantiques. Après quelques recherche, on tombe sur 2 journaux : [La Muse française](https://fr.wikipedia.org/wiki/La_Muse_fran%C3%A7aise) et [Le Conservateur littéraire](https://fr.wikipedia.org/wiki/Le_Conservateur_litt%C3%A9raire).

## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{le_conservateur_litteraire}
```