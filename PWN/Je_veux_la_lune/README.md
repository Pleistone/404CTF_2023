# Je veux la lune !

**Difficulté** : Introduction

## Enoncé

Caligula est assis seul devant une table du café. Il y a devant lui 5 tasses vides empilées, et une 6e qu'il sirote lentement, ainsi qu'un ordinateur qu'il regarde fixement. Des cernes profonds creusent son visage. Il lève des yeux étonnamment vifs vers vous alors que vous vous approchez de lui.

Il tend sa main vers son écran d'un air désespéré et s'exclame « Je ne peux plus vivre comme ça, ce monde n'est pas supportable. J'ai besoin de quelque chose de différent. Quelque chose d'impossible, peut-être le bonheur, ou peut-être la lune... Et je sens que ma quête s'approche de sa fin. »

Vous regardez son écran, et voyez qu'il tente d'accéder sans succès à un fichier.

« Vous pensez que je suis fou, mais je n'ai jamais pensé aussi clairement ! » Un calcul rapide vous informe qu'il a probablement consommé plus d'un litre de café, et il n'est que 13h. Vous acquiescez lentement. Il reprend « Regardez, Hélicon m'a enfin rapporté la lune, mais il ne m'a pas donné l'accès... le fourbe. Je brûlerai un quart de sa fortune plus tard pour le punir. Aidez-moi ! »

Entre peur et pitié, vous décidez de l'aider à obtenir le contenu du fichier secret.


## Solution

En ressouce du challenge, un script shell est fournit. En analysant son fonctionnement, on constate que l'entrée `personne` n'est pas sanitize. Cela signifie que l'on peut injecter du code dans cette entrée, qui sera ensuite exécuté lors de l'appel à la ligne `eval grep -wie ^$personne informations.txt`. Selon l'énoncé, Caligula souhaite obtenir la lune, donc on affiche le contenu du fichier `lune.txt` avec la commande : `echo $(<lune.txt)`.

On établit dnc la connextion avec le serveur avec la comande `nc challenges.404ctf.fr 31215` et on envoie `echo $(<lune.txt)` 
<p align="center"><img src="Solution.png" alt="Solution" width="800"></p>

## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{70n_C0EuR_v4_7e_1Ach3R_C41uS}
```
