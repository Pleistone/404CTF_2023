# Art

**Difficulté** : Introduction

## Enoncé

Trois hommes sont attablés dans un coin du café. L'un d'eux, Serge, sort une tablette et montre avec beaucoup de fierté sa nouvelle acquisition : un NFT "blanc avec des liserés blancs transversaux". Ses deux amis ne semblent pas convaincus par cet achat :

<p align="center"> MARC  
<br> Cher ? </p>

<p align="center"> SERGE   
<br> Deux cent mille. </p>

<p align="center"> MARC   
<br> Deux cent mille ?... </p>

<p align="center"> [...] </p>

<p align="center"> SERGE 
<br> Mais mon vieux, c'est le prix. C'est un ANTRIOS ! </p>

<p align="center"> MARC   
<br> Tu n'as pas acheté ce tableau deux cent mille francs ! </p>

<p align="center"> SERGE   
<br> J'étais sûr que tu passerais à côté. </p>

<p align="center"> MARC    
<br> Tu as acheté cette merde deux cent mille francs ?! </p>

Qui achèterait une telle oeuvre d'art ? Qui VENDRAIT une telle oeuvre d'art ?   
Trouvez l'adresse Ethereum de l'artiste.   
> Format : 404CTF{adresse}


## Solution

On doit trouver l'adresse Ethereum  de l'artiste. On utilise le site web [opensea](https://opensea.io/) pour trouver l'oeuvre. On recherche les mots clé "blanc avec des liserés blancs transversaux" qui semble être le nom du NFT acheté. Voici les premiers résultats :

<p align="center"><img src="NFT recherche.png" alt="NFT recherche" width="500"></p>

Les NFT unicolores appartiennent à Antrios, l'artiste mentionné dans l'énoncé. Sur [son profil](https://opensea.io/Antrios), on obtient son adresse Ethereum : 0xD7186D588Ed2AddF8b260d09B108100f264A64A9

## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{0xD7186D588Ed2AddF8b260d09B108100f264A64A9}
```
