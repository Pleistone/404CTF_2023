# Cache-cache : le retour

**Difficulté** : Moyen

## Enoncé

Vous poursuivez votre chemin dans le café littéraire lorsque vous remarquez une table intrigante. Vous croyez y reconnaitre Georges Perec, connu pour son amour des jeux de mots et des énigmes. Vous vous approchez et entamez une conversation avec lui. Après quelques échanges, vous attirez son attention et il vous invite à une soirée qu'il organise avec Marcel Pagnol au célèbre Château de La Buzine. Cependant, en dépliant l'invitation, vous réalisez qu'un mot de passe est requis pour accéder à l'événement. Vous décidez de vous creuser les méninges pour résoudre cette énigme avant le jour de la fête, sans succès.

Le jour de la fête, vous vous cachez près de l'entrée du château dans l'espoir d'entendre les mots de passe proposés par les autres invités qui arrivent un à un, mais vous constatez que chaque mot de passe est différent. Cependant, étant convaincu que Georges Perec et Marcel Pagnol n'auraient pas créé cette énigme sans qu'il y ait un lien entre tous ces mots de passe, vous gardez espoir.

Après un moment, vous vous approchez de l'entrée du château, vous préparant à donner le mot de passe que vous aurez réussi à déchiffrer.

PS : Un peu de bon sens, ne venez pas les mains vides. Et surtout, n'oubliez pas de jeter un coup d'œil dans la salle_au_tresor lorsque vous déposerez votre cadeau. Vous pourriez y trouver quelque chose d'intéressant !

Toutes les informations nécéssaires à la résolution de ce challenge sont présentes après s'être connecté en netcat.


## Solution

On commence par exécuter le fichier pour observer le comportement du programme :

<p align="center"><img src="Execution du programme.png" alt="Execution du programme" width="800"></p>

Après avoir testé le fonctionnement du programme, on se lance dans une analyse approfondie en décompilant le programme `cache_cache_le_retour` avec Ghidra. Tout d'abord, il est nécessaire de trouver un mot de passe. Ce mot de passe est généré selon un certain algorithme qui utilise des nombres aléatoires générés à partir d'un seed. Cette seed est basé sur l'heure actuelle précise à la seconde prêt, elle est obtenue grâce à la fonction `time(0)`. Ainsi, si on recode exactement cet algorithme et qu'on le lance simultanément avec la commande `nc challenges.404ctf.fr 31725`, on serat en mesure d'obtenir le mot de passe à fournir au Portier. Cet algorithme est recodé dans ``

Dans un second temps, on se retrouve face à un garde, et il nous faut envoyer la base64 d'un fichier zip nommé `mystere.zip`, contenant un fichier appelé `surprise.txt`. En retour, le programme affichera le contenu de "surprise.txt". Afin d'accéder à la salle au trésor, on utilisera la vulnérabilité "zip symbolic link", qui consiste à faire de `surprise.txt` un lien symbolique vers le fichier `salle_au_tresor`. Ainsi, lorsque le programme ouvrira le zip et cherchera à lire le contenu de "surprise.txt", il sera redirigé vers "salle_au_tresor". Pour créer un tel zip, on utilise les commandes suivantes :

```shell
echo 'mon message' > salle_au_tresor
ln -s salle_au_tresor surprise.txt
zip --symlinks test.zip surprise.txt
```

Une foit cela fait le flag s'affiche.

## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{UN_CH3V41_D3_7r013_P0Ur_3NV4H1r_14_54113_4U_7r350r}
```