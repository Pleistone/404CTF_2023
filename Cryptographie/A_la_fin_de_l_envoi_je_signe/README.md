# À la fin de l'envoi, je signe !

**Difficulté** : Difficile

## Enoncé
Alors que vous étiez entrain de vous diriger vers la sortie du café, vous entendez subitement du bruit venir d'un petit attroupement formé autour d'une table. Un homme, debout, semble visiblement agaçé par quelque chose.   
« C'est inadmissible ! Comment je peux me défendre maintenant ? Si je répond à leurs critiques, ils me traiteront de troll !   
— Calme-toi Pierre, tu sais bien que ça nous gène tout autant que toi.   
— C'est une insulte, c'est un affront, que dis-je, c'est une hérésie !   
— T'en fait toujours trop, souris celle dont vous vous souvenez qu'elle s'appelle Marthe.   
— Qu'est-ce qu'il se passe ? Demandez-vous en vous rapprochant de la conversation.   
— Salutations à vous, vous répondis Pierre en vous saluant avec son chapeau. Nous sommes dans une situation terrible ! Nous possédions un système de signature très avancé au sein du groupe qui nous permettait de signer des messages au noms du groupe. Malheureusement, l'ancien administrateur du système est parti, et nous n'avons plus le contrôle dessus. J'ai l'habitude de me défende contre toute sorte de viles critiques quant aux ouvrages que je produis, mais maintenant que je ne peux plus signer mes réponses, je vais perdre toute crédibilité ! Pauvre de moi !   
— Je peux essayer de regarder ce système si vous voulez.   
— Vous pensez pouvoir reprendre la main dessus ? Si vous y arriviez, vous aurez ma reconnaissance éternelle !   
— Ça vaut le coup d'essayer ! Répondez vous en souriant, amusé par la grandiloquence du bonhomme. »   


## Solution

Ce challenge traite du schéma de signature à usage unique Winternitz. Ce schéma utilise des chaînes de hashs, de la façon suivante :  
Imaginons que je veuille signer un message M composé d'un blocs de 4 bits (0 ≤ nb_bits(M) < 2^block_size). Je me fais une clé privée `Kpriv=H(random)`, et je calcule la clé publique en appliquant 16=2^block_size fois un algorithme de hachage H sur Kpriv, `Kpub = H(H(H(H...(H(Kpriv))))) = H^16(Kpriv)`. Pour signer M (0 ≤ nb_bits(M) ≤ 2^block_size), on calcule `S = H^M(Kpriv)`. Cette signature est facile à vérifier, en vérifiant que `H^(16-M)(S) == Kpub`. Si c'est le cas, c'est que le signataire était en possession de Kpriv. Attention toutefois, une fois qu'une signature a été générée, il est facile pour un attaquant de signer un message M' plus grand que M (en appliquant simplement la fonction de hashage M' - M fois)

Pour appliquer ce schéma de signature à un message plus long, il suffit de répéter l'opération sur chaque bloc (c'est plus facile que de simplement augmenter la taille de bloc, qui augmenterait exponentiellement le nombre d'opérations de hachage à effectuer). Ainsi, la clé privée est un tableau `[Kpriv_0, Kpriv_1, Kpriv_2, ...]` et la clé publique `[Kpub_0, Kpub_1, Kpub_2, ...]`, chaque sous-clé étant responsable de la signature d'un bloc comme vu plus haut.

Pour palier au problème évoqué plus haut sur la capacité d'un attaquant à signer un message "plus grand", une checksum est ajoutée. Celle-ci fonctionne "à l'envers", de sorte que la checksum associée à un "petit message" soit grande, et celle d'un "grand message" soit petite, afin que signer un "plus grand" message nécessite de remonter la chaîne de hashs pour la partie relative à la checksum. 

Toutefois, cette signature reste à usage quasi-unique, parce qu'à partir du moment où un attaquant a vu passer deux couples (petit message, grande checksum) et (grand message, petite checksum), il peut avancer les chaînes de hashs des deux côté et signer quasiment n'importe quel message. C'est précisément cette vulnérabilité que l'on va exploiter ici étant donné que l'on connaît la signature du message "SALUT CA VA?", cette attaque est implémenté dans le fichier `solve.py`.


## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{Wint3r_i5_c0m1ng}
```