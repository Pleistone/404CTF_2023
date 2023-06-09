# La Quête du sens [1/3]

**Difficulté** : Facile

## Enoncé

Vous êtes assis à côté d'une femme - Mar-quelque chose, vous n'avez pas retenu son prénom - qui fredonne doucement. Il vous semble que vous connaissez cet air.   
Retrouvez le nom du texte dont est issue la chanson.

> Format : 404CTF{nom_du_texte}

## Solution

### Solution 1 
On nous fournit un seul fichier mp3. En utilisant SoundHound beaucoup de fois, on parvient finalement à identifier une chanson française correspondante. Cette chanson s'avère être "Les Séparés" de Julien Clerc. À partir du titre de la chanson, il est facile de retrouver le nom du texte dont elle est issue.

### Solution 2
Une approche plus efficace consiste à analyser attentivement l'énoncé. On recherche une écrivaine dont le nom commence par "Mar" et qui a écrit des textes adaptés en chanson. Après quelques recherches, on découvre Marceline Desbordes-Valmore. Elle a écrit un texte intitulé "Les Séparés", qui a été adapté en musique par Julien Clerc.

## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{les_separes}
```