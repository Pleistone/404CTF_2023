# Fuite en 1791

**Difficulté** : Moyen

## Enoncé

Alors qu'une douce odeur de café commençait à emplir Le Procope, une femme vient interrompre le calme de la chaleureuse pièce. Tout droit sortie du XVIIIème siècle, Olympe de Gouge fait irruption et se précipite vers votre table.

« Vous ! s’écria-t-elle  
— Moi ? répondez-vous.  
— Oui vous, allez porter cette lettre de toute urgence à Anne-Catherine Helvétius.  
— Qui ? De quoi s'agit-il ?  
— Je ne peux vous expliquer maintenant, mais le contenu de cette lettre peut changer le cours de l'histoire, ne perdez pas de temps. »

Et avant même que vous puissiez la questionner d'avantage, elle passa la porte et sortit du café.

Dans l'incompréhension la plus totale, vous commencez à parcourir ladite lettre…

Toutes les informations nécessaires à la résolution de ce challenge sont présentes dans l'énoncé ci-dessus.

> <p align="center"> https://ddfc.challenges.404ctf.fr </p>


## Solution

Pour ce challenge, nous arrivons sur une page avec rien d'intéressant à part un lien redirigeant vers une autre page.  On tombe alors sur un message qui nous dit lien expiré.

<p align="center"><img src="Expired link.png" alt="Expired link" width="500"></p>

Il faut donc probablement trouver un moyen d'acceder a cette page. En examinant de plus pret le lien qui nous a mener vers celle-ci `https://ddfc.challenges.404ctf.fr/ddfc?expiry=-5625891076&signature=wawF6dC4Hz9g5NyCc3j1KCDcfztFE/sp` on peut voir qu'il y a une parametre `expiry=-5625891076`, le nombre 5625891076 étant un timestamp correspondant a la date du 21/09/1791 à 12:38:05. On teste d'acceder a la page en modifiant cette valeur pour une valeur plus recente, comme 5625891076 (qui correspond à la date du 11/04/2148 12:31:16) on à une autre erreur :  

<p align="center"><img src="Invalid signature.png" alt="Invalid signature" width="500"></p>

Il faudra donc faire preuve de plus de subtilité dans la manière de modifier l'URL. Après quelques recherches, on découvre rapidement une vulnérabilité appelée "[parameter-pollution](https://book.hacktricks.xyz/pentesting-web/parameter-pollution)". Elle consiste à inclure plusieurs fois le même paramètre, ce qui peut entraîner différentes vulnérabilités selon la façon dont le parsing est réalisé.

On effectue donc une requête sur l'URL suivante : `https://ddfc.challenges.404ctf.fr/ddfc?expiry=-5625891076&signature=wawF6dC4Hz9g5NyCc3j1KCDcfztFE/sp&expiry=5625891076`. Cette fois-ci, le lien fonctionne et on est dirigé vers une page où le flag se trouve à la fin.

<p align="center"><img src="Flag page.png" alt="Flag page" width="500"></p>


## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{l4_p011uti0n_c_3st_m41}
```
