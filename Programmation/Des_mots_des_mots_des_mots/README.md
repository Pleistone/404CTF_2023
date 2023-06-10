# Des mots, des mots, des mots

**Difficulté** : Difficile

## Enoncé

Prenant du bon temps à votre table en lisant un livre, vous buvez une gorgée de café. En baissant votre tasse, vous remarquez à travers la fenêtre une petite silhouette, elle semble chercher quelque chose ou quelqu'un.

Cette intrigante situation vous pousse à aller à sa rencontre. La silhouette est en réalité une jeune fille rousse. Vos regards se croisent, elle a l'air perdue. Vous la rejoignez, et lui demandez :

« Bonjour, puis-je t'aider ?   
— Oui. Je cherche à traduire un texte selon des règles étranges mot à mot. Il s'agit d'un livre nommé Les Misérables. Peux-tu m'aider ? Au fait, moi c'est Cosette !   
— Je vois, aucun problème. Je peux justement te faire un script qui va transformer chaque mot de ton texte. Quelles sont ces règles ?   
— Je vais tout t'expliquer, allons nous installer à l'intérieur.»

Elle vous suit à votre table et vous vous mettez au travail.

Indications :   
- Les voyelles sont {a, e, i, o, u, y}.   
- L'indiçage commence à 0.   
- Les règles sont données en Markdown. Les _ dans les exemples sont des balises italique Markdown et ne comptent pas dans l'exemple.   
- Les règles sont à appliquer les une après les autres. Typiquement pour la règle 2 il faut partir du résultat de la règle 1, et ainsi de suite.   
- Le symbole ^ correspond à l'opérateur puissance.

## Solution

Pour résoudre ce challenge, on se connecte au serveur à l'adresse `challenges.404ctf.fr:31420`. On nous donne ensuite les règles que nous devons appliquer pour traduire un mot. Une fois que la liste des règles nous a été donnée, le serveur nous envoie une grande liste de mots que nous devons traduire en quelques secondes. Voici la liste des règles :   
Règle 0 : Aucune modification   
Entrée : {cosette}  Sortie : {cosette}

Règle 1 : Inverser les lettres   
Entrée : {cosette}  Sortie : {ettesoc}

Règle 2 :   
- Si le mot à un nombre de lettres pair, échanger la 1ere et la 2e partie du mot obtenu   
- Sinon, enlever toutes les lettres du mot correspondant à la lettre centrale   
Entrée : {ettesoc}  Sortie : {ttsoc}

Règle 3 :
Si le mot a 3 lettres ou plus :   
- Si la 3e lettre du mot obtenu est une consonne, "décaler" les voyelles vers la gauche dans le mot original, puis réappliquer les règles 1 et 2.   
- Sinon : la même chose mais les décaler vers la droite.   
Entrée : {ttsoc}  Sortie : {ottsc}

Règle 4 :
- Pour `n` allant de 0 à la fin du mot, si le caractère `c` à la position `n` du mot est une consonne (majuscule ou minuscule), insérer en position `n+1` le caractère de code ASCII `a = ((vp + s) % 95) + 32`, où `vp` est le code ASCII de la voyelle précédant la consonne `c` dans l'alphabet (si `c = 'F'`, `vp = 'E'`), et `s = SOMME{i=n-1 -> 0}(a{i}*2^(n-i)*Id(l{i} est une voyelle))`, où `a{i}` est le code ASCII de la `i`-ième lettre du mot, `Id(x)` vaut `1` si `x` est vrai, `0` sinon, et `l{i}` la `i`-ième lettre du mot. Attention à bien appliquer cette règle aussi sur les caractères insérés au mot.
Entrée : {ottsc}  Sortie : {PPtt!15QRUWcos}

Une implémentation des règles peut être trouvées dans le fichier `rules.py`, et l'algorithme de résolution du challenge est dans `solve.py`.


## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{:T]cdeikm_)W_doprsu_nt_;adei}
```