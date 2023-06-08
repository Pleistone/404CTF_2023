# Trois

## Enoncé

Lors de votre exploration du Procope, vous sentez une légère agitation parcourir la salle. Il semblerait qu'une membre éminente du café, surnommée Louise Michel, ait disparu récemment, en laissant derrière elle une lettre :

*Trois.  
C'est le nombre de côtés d'un triangle.  
C'est partout.  
C'est nul part.  
C'est le nombre de romans que j'ai écrit au Bagne.  
C'est le nombre de lettres du RSA.  
C'est la base de tout.*

Ainsi qu'une série de chiffres : 

`ct=19927008564294677002520448437970189702487045648296885900114209856216930305451618124458156678801175987674123914659764210541248496719249933402823789713001815042047073138247252659866129206243219671633681286208956499952633370685989888960098084954742719978788425463076280549248624761445797200322025774847601077501261839135577696465884169289996756953347035809346587936831552564678928269851681275066679507994429117368820892833335277246964370806184539958497154299718109950045195337068953209732230159909730862209492939796706112091048490516753954885137398037737716953735239767024153079083060887610014817408325631010848848643987`

`e=0x13333`

`n=27584244764354155600648132819557552425739308915389010331967630630278781451355292616283908233886829051620691675066793826289384271685368839532793120327210935428497022861038124315374145401503459557634600149428324393706219187751525385285666118615589270213292021952450269684503014960000456627468842728153985933435658303773466724122153491920323012054102145457826086103327235133218830942039915609182594401161042859134214824202027169450776481815084629313897269088778093661872262506720997309450453842156237745662622884714477231701108303167577929395851134011771107866535083165178026955131807919002588840216970211283961590847119`

Pourriez-vous aidez ses amis, qui sont inquiets pour elle? 

## Solution

On retrouve ici les paramètres classiques d'un cryptosystème RSA, avec la clé publique (n, e) et le ciphertext. Il faut donc casser ce RSA. Le titre et l'énoncé semblent indiquer qu'il se passe quelque chose avec le nombre 3. Effectivement, observer n en base 3 donne un résultat remarquable: elle est très vide, et contient majoritairement des 0. On peut se servir de cette observation pour essayer de transformer ce problème en un problème de factorisation de polynômes. En effet, la factorisation de polynômes est un problème plus simple que celui de la factorisation d'entiers. Ainsi, en transformant cette représentation en un polynôme P(X) de telle sorte à ce que l'on ait n = P(3), on se retrouve avec un polynôme possédant très peu de coefficients non nuls relativement à son dégré plutot élevé (1293). On peut donc espérer factoriser ce polynôme P en deux facteurs P1 P2, qui une fois évalués en 3 nous donnerons les facteurs de n, suffisant pour retrouver le clé privée et résoudre le challenge. 

Cette solution est implémentée dans `solve.sage`, pour le lancer utiliser la commande `sage solve.sage`.

## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{Un_D3ux_7R015_P13rr3_P4ul_37_M4r13}
```