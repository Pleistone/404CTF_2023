# Le Jour de l'espace

## Enoncé

Rimbaud vous propose une séance initiatique au Oui-ja dans l'aile mystique du café littéraire (oui, oui, ça existe), vous avez une vision ésotérique :   
Alors que vous voyez le texte suivant **ueomaspblbppadgidtfn**, Rimbaud vous décrit voir un étrange cadre de 50cm de côté, avec des petits carrés de 10cm de côtés, numérotés de 0 à 24 et jetés pêle-mêle sur le sol. Rimbaud n'y comprends rien, mais vous restez obsédé par cette idée, et décidez de résoudre l'énigme.

> Format : 404CTF{cequevousalleztrouver}

## Solution

### Solution 1 

Comme indiqué dans l'énoncé, on constate le serveur en utilisant la commande `nc challenges.404ctf.fr 31451`. Le serveur nous invite ensuite à envoyer un texte en clair, et en retour, il nous renvoie le texte chiffré correspondant. On comprend donc qu'il nous faut comprendre le fonctionnement du chiffrement en effectuant des tests, afin de pouvoir déchiffrer ultérieurement le texte **ueomaspblbppadgidtfn**.

On commence par envoyer des messages très courts, composés d'une ou deux caractéres. On remarque alors que les seules caractéres acceptées sont les lettres de "a" à "y". De plus à chaque fois que l'on recois une réponse elle est de cinq lettres. En effectuant des tests sur des mots dont l'on augmente progressivement la taille, on comprend rapidement que l'algorithme chiffre les cinq premières lettres, puis les cinq suivantes, et ainsi de suite, puis concatène les chiffrés.

En poursuivant nos tests, on constate que l'ajout de la lettre "a" à la fin d'un mot n'affecte pas le chiffrement tant que la taille du mot ne dépasse pas le prochain multiple de cinq. On en conclu que l'algorithme utilise la lettre "a" pour effectuer un padding sur le mot afin de le rendre d'une taille multiple de cinq.   
Exemple : chiffré(monmot) = chiffré(monmo) + chiffré(taaaa)

On a donc juste à comprendre comment l'algorithme chiffre un mot de 5 lettres.

Dans l'objetif de mieux comprendre le chiffrement, on développe un algorithme Python qui convertit chaque lettre du mot en son indice dans l'alphabet. Par exemple, la conversion de "abcd" donne [0 1 2 3]. Nous commençons par l'appliquer sur des messages courts.

On fait alors les constats suivants :
- chiffré(c)=chiffré(caaaa)=2\*chiffré(baaaa)=2\*chiffré(b)
- chiffré(d)=chiffré(daaaa)=3\*chiffré(baaaa)=3\*chiffré(b)
- chiffré(e)=chiffré(eaaaa)=4\*chiffré(baaaa)=4\*chiffré(b)

- chiffré(ac)=chiffré(acaaa)=2\*chiffré(abaaa)=2\*chiffré(ab)
- chiffré(ad)=chiffré(adaaa)=3\*chiffré(abaaa)=3\*chiffré(ab)
- chiffré(ae)=chiffré(aeaaa)=4\*chiffré(abaaa)=4\*chiffré(ab)

On comprend alors que le chiffrement d'un mot de 5 lettres fonctionne selon l'exemple suivant : **chiffré(txays) = indice(t)\*chiffré(baaaa) + indice(x)\*chiffré(abaaa) + indice(a)\*chiffré(aabaa) + indice(y)\*chiffré(aaaba) + indice(s)\*chiffré(aaaab)**

Maintenant, que nous avons compris le fonctionnement du chiffrement, on pourrait chercher à l'inverser en utilisant des matrices, ce qui serait tout à fait faisable. Cependant, nous allons opter pour une solution alternative. En effet, nous savons qu'il existe un nombre fini de chiffrements possibles pour un mot de 5 lettres (25^5 = 9 765 625). Ainsi, si nous chiffrons un mot, puis chiffrons le résultat et ainsi de suite, en répétant l'opération un nombre suffisant de fois (au maximum 25^5 fois) on finira par retomber sur le mot d'origine. Pour obtenir la version déchiffrée du mot de départ, il suffit de récupérer le résultat que nous avons obtenu juste avant de retomber sur le mot de départ. Étant donné que nous connaissons l'algorithme de chiffrement, nous pouvons réaliser ces opérations de chiffrement très rapidement. Nous appliquons ce principe à chaque groupe de cinq lettres de notre mot, puis nous concaténons les résultats pour obtenir la version déchiffrée du mot.

Cette solution est implémentée dans `solve1.py`.


### Solution 2 

Dans cette approche, nous commençons par effectuer les mêmes tests que dans la solution précédente. Une fois que nous avons compris que le mot est chiffré par groupes de cinq lettres, nous réalisons qu'il n'y a que 25^5 = 9 765 625 combinaisons de 5 lettres entre "a" à "y" possibles. On crée alors une chaîne de caractères de taille 5 * 9 765 625, contenant toutes les combinaisons possibles, que nous envoyons au serveur. Si jamais la chaîne avait été trop longue pour le serveur, on aurait pus essayer de la découpe en plusieurs chaînes un peu plus petite. Le serveur nous renvoie le chiffrement de cette très longue chaîne. Nous n'avons plus qu'à découper la réponse en groupes de cinq lettres, ce qui nous donne pour chaque combinaison de 5 lettres le chiffrement correspondant.

Pour déchiffrer notre mot, nous le découpons également en groupes de cinq lettres, puis nous recherchons chaque morceau dans la liste des chiffré puis on regarde quel est la version déchiffrée correspondante.


## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{barjavelmaassassine}
```

