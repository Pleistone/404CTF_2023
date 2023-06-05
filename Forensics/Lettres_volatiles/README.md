# Lettres volatiles

## Enoncé
Une femme regarde avec hésitation une table à l'autre bout du café Le Procope, au milieu des conversations de fond des habitués. Sur cette table, un ordinateur allumé est laissé à l'abandon.

<p align="center"> ARSINOÉ </p>

<p align="center"> à part </p>

<p align="center"> Vais-je réellement croissanter mon amie ? </p>

<p align="center"> Je m'en voudrais longtemps, même si c'est permis. </p>

<p align="center"> Cela suffit. Il est grand temps que je m'élance. </p>

<p align="center"> De Célimène, je vais trahir la confiance. </p>

<p align="center"> ARSINOÉ </p>

<p align="center"> prenant les commandes de la machine </p>

<p align="center"> Il semble que quelques intéressants fichiers </p>

<p align="center"> Soient protégés par quelque magie noire. </p>

<p align="center"> Célimène garde vraiment bien ses secrets. </p>

<p align="center"> Il va alors falloir capturer sa mémoire. </p>



## Solution

Le titre de l'énoncé annonce l'aise entre que l'on vas utiliser volatility. Comme on nous indique que les données que l'on cherche sont des données utilisateur, on s'attend à trouver un dump mémoire dans le système de fichier, car on parle d'une capture de mémoire.

Comme on cherche des données utilisateur, on va dans des répertoires bien connus comme notamment Images, Téléchargements, Documents,...
Dans Images, on trouve le magnifique logo, et un png d'un drapeau, après analyse l'image ne semble rien contenir de particulier.
On fini par trouver un fichier `s3cr37.zip` dans le dossier /documents/perso.

On essaye de le décompresser, mais il requiert un mot de passe. On peut obtenir plus d'information sur le zip avec la commande `zipdetails s3cr37.zip` on vois qu'il est chiffré avec une clé AES, on a donc peu de chances de pouvoir la cassé. On peut néanmoins essayer avec `fcrackzip -v -D -p rockyou.txt -u s3cr37.zip`, mais ce n'est pas concluant.

On reprend nos recherches et on trouve un dossier jumpbag qui après des recherches sur Internet, on apprend sert à dump la ram. On y trouve un fichier .raw.
On analyse le dump mémoire avec volatility, on commence avec la commande `vol2 -f C311M1N1-PC-20230514-200525.raw imageinfo` pour récupère diverses informations sur la machine.
Après avoir regardé un peu ce que contient le dump on se demande où pourrais se trouver un mot de passe, on se dit quoi pourrait être dans le presse-papiers, car on a tendance à copier-coller des mots de passe, pour récupère le contenu du clipboard on entre la commande suivante `vol2 -f imageinfo vol2 -f --profile Win7SP1 clipboard`.
On y trouve le mot de passe du zip : `Z1p p4s5wOrd : F3eMoBon8n3GD5xQ`.

On ouvre le zip avec la commande `7z x s3cr37.zip` (on est obligé d'utiliser cette commande, car la commande zip ne supporte pas les clés AES).
Il contient un pdf dans lequel on trouve le flag

## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{V0147i1I7y_W1Ll_N3v3r_Wr8_loV3_l3ttEr5}
```