# Les OSINTables 1/3

**Difficulté** : Facile

## Enoncé

En pleine discussion au Procope, Cosette vous raconte autour d'une part de fraisier la première fois qu'elle a essayé d'envoyer une lettre à son bienfaiteur : Jean Valjean.

Débutante dans la démarche postale, elle s'est trompée sur les informations nécessaires, elle en a même oublié l'adresse du destinataire, n'écrivant que la sienne. Elle vous montre la photo ci-jointe et vous met au défi de trouver d'où elle l'a écrite.
 
Trouvez l'adresse d'envoi de la lettre (celle de Cosette).
> Format : 404CTF{numero_adresse_rue_ville} 

_exemple : 404CTF{36_quai_des_orfevres_paris}_


## Solution

On nous fournis l'image suivante :
<p align="center"><img src="photo.jpg" alt="Photo Lettre" width="400"></p>

Sur cette lettre on peut voir Divers information :
- Le nom de la rue : Rue Victor Hugo
- Le numéro de rue : LXXXIII = 83
- Le début du nom de la ville : Ve
- Le début d'un numéro de téléphone : 04

On cherche donc l'adresse 83 Rue Victor Hugo dans une ville commencent par "Ve" situer dans la zone en France ou les téléphone sont en 04, c'est-à-dire le sud de la France. En cherchant un lieu qui répond a tous ces critères sur Google Map, on tombe sur le 83 Rue Victor Hugo à Vergèze.

## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{83_rue_victor_hugo_vergeze}
```