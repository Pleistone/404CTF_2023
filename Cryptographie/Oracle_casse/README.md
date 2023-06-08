# Oracle cassé

## Enoncé

Cette description fait référence à un challenge de l'édition précédente qu'il n'est absolument pas nécessaire de connaître pour faire ce challenge.

Nous souhaitons prendre la parole pour vous dire que nous avons compris vos plaintes concernant les oracles de l'édition précédente. Nous comprenons que ces derniers ont été jugés injustes et trop difficiles à deviner, et c'est pourquoi nous avions décidé de les retirer. C'est pourquoi nous avons décidé de refaire un nouvel oracle, avec les toutes dernières technologies d'optimisation à notre disposition. Afin de nous excuser pour la gène occasionnée, nous offrons aux 1000 premiers arrivés un cadeau à récupérer directement dans l'oracle. Par souci de transparence, nous vous fournirons cette fois-ci le code de fonctionnement exact de cet oracle.

Nous vous prions d'agréer, Madame, Monsieur, l'expression de nos salutations distinguées.   
Colette, directrice du Matin et du 404CTF

## Solution

Dans le fichier "oracle.py", on trouve l'algorithme appliqué par l'oracle, auquel on peut accéder en utilisant la commande `nc challenges.404ctf.fr 31451`.   
Après analyse, nous comprenons que l'oracle effectue les actions suivantes :   
- Il commence par générer une paire de clés publique/privée pour RSA.   
- Ensuite, il utilise RSA pour chiffrer le flag avec cette clé.   
- Il affiche la valeur chiffrée du flag et la représentation hexadécimale de la clé publique.   
- Ensuite, il nous demande ce que l'on veut lui envoyer.   
- Il applique un algorithme qui ressemble à un algorithme de signature RSA, mais en réalité, il contient une petite erreur qui produit un résultat incorrect.   
- Enfin, il affiche le résultat de l'algorithme.

Si la fonction de signature avait été implémentée correctement, il aurait suffi d'envoyer le chiffré du flag pour obtenir le flag. Cependant, cette erreur dans le code de l'algorithme de signature ouvre une autre opportunité. Elle permet d'appliquer une technique appelée [rsa fault attack](https://medium.com/asecuritysite-when-bob-met-alice/beware-of-rsa-fault-attacks-they-may-comprise-your-trust-infrastructure-cf61c57f5c28), qui consiste à partir d'une signature fausse pour trouver l'un des facteurs de la clé publique et ainsi en déduire la clé privée. Une fois que nous avons la clé privée, il est facile de déchiffrer le message avec RSA.

C'est ce qui est implementé dans `solve.py`.

## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{Un_0r4cl3_vr41m3n7_c4553_c3773_f015}
```
