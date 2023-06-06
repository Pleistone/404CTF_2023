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

Dans l'énoncé, il est spécifié que les données recherchées sont des données utilisateur, et il est également fait référence une capture mémoire. De plus, le titre de l'énoncé suggère l'utilisation de Volatility. Par conséquent, on peut s'attendre à trouver un dump mémoire dans le fichier zip fournit.

Comme on cherche des données utilisateur, on va dans des répertoires classiques comme Images, Téléchargements, Documents...
Dans Images, ont un png de drapeau, après analyse l'image ne semble rien contenir de particulier.
En continuant les recherches, on fini par trouver un fichier s3cr37.zip dans le dossier /documents/perso.

On peut tenté de le décompresser, mais un mot de passe est requit. Pour obtenir plus d'informations sur le fichier zip, on utilise la commande `zipdetails s3cr37.zip`. Cette commande nous révélé que le fichier est chiffré avec une clé AES, ce qui rend peu probable notre nos chances de casser la clé. Néanmoins, on peut essayé avec la commande `fcrackzip -v -D -p rockyou.txt -u s3cr37.zip`, mais cela n'abouti à rien. 

On poursuit nos investigations, on fini par découvrir un dossier nommé "jumpbag". Après des recherches sur Internet, on apprend que ce dossier sert à dump la ram. On y trouve un fichier .raw. On analyse le dump mémoire avec volatility 2. On commencé par exécuter la commande `volatility -f C311M1N1-PC-20230514-200525.raw imageinfo` pour obtenir diverses informations sur la machine.

<p align="center"><img src="Volatility imageinfo.png" alt="Volatility imageinfo" width="800"></p>

`volatility -f C311M1N1-PC-20230514-200525.raw pslist`

On regarde les différents processus contenu du dump mémoire avec la commande `volatility -f C311M1N1-PC-20230514-200525.raw pslist`, et on s'interroge sur ou on pourrait trouver un mot de passe.

<p align="center"><img src="Volatility processus.png" alt="Volatility processus" width="800"></p>

 Après réflexion, on envisage qu'il se trouve dans le presse-papiers, étant donné notre tendance à copier-coller des mots de passe. Pour extraire le contenu du presse-papiers, on utilise la commande suivante : `volatility -f C311M1N1-PC-20230514-200525.raw --profile Win7SP1 clipboard`. Eurêka, on y trouve bien le mot de passe du zip : Z1p p4s5wOrd : F3eMoBon8n3GD5xQ.

On décompresse le zip avec la commande `7z x s3cr37.zip` puis le mot de passe, on ne peut pas utiliser la commande unzip ici, car elle ne supporte pas les clés AES.
Le zip contient un pdf dans lequel on trouve le flag.

## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{V0147i1I7y_W1Ll_N3v3r_Wr8_loV3_l3ttEr5}
```