# La Réponse de Voris

## Enoncé

Vous rencontrez Mme de Beauvoir qui vous explique vouloir surprendre son mari Jean Sol Partre. Ce dernier est en train d'écrire un livre et a demandé à son ami Voris un titre approprié. Elle a réussi à se procurer un étrange message, qu'elle pense avoir été chiffré par Voris afin de limiter les fuites d'information. Ne sachant quoi faire avec ceci, elle s'est décidée à aller à la séance de spiritualisme du samedi au café littéraire, où elle vous a rencontré aujourd'hui. Par chance, vous connaissez une oracle pouvant peut être vous aider à déchiffrer ce message. Mais, malchance, cette dernière n'est qu'en mesure de chiffrer un message... Dommage, il va falloir réfléchir pour trouver le titre que Voris a proposé à Jean Sol !

> Format : 404CTF{titre_du_livre}

> message chiffré : pvfdhtuwgbpxfhocidqcznupamzsezp


## Solution

Comme indiqué dans l'énoncé, on constate le serveur en utilisant la commande `nc challenges.404ctf.fr 31682`. Le serveur nous invite ensuite à envoyer un texte en clair, et en retour, il nous renvoie le texte chiffré correspondant. On comprend donc qu'il nous faut comprendre le fonctionnement du chiffrement en effectuant des tests, afin de pouvoir déchiffrer ultérieurement le texte **ueomaspblbppadgidtfn**.

On commence par envoyer des messages très courts, composés d'une ou deux caractéres. 


## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{lenclumedesjourneesensoleillees}
```
