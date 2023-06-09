# Les Mystères du cluster de la Comtesse de Ségur [1/2]

**Difficulté** : Facile

## Enoncé
Vous rencontrez la Comtesse de Ségur au Procope. La Comtesse de Ségur a créé une entreprise de vente de livres en ligne en s'aidant du succès de ses livres pour enfants et l'a déployé sur un cluster Kubernetes.

Celle-ci vous explique avoir été victime d'une demande de rançon. En effet, quelqu'un lui a volé ses livres pas encore publiés et menace de les publier sur Internet si elle ne lui paye la rançon demandée.

La Comtesse vous demande d'enquêter sur la manière dont le maître chanteur a pu voler ses livres et vous donne pour cela les informations à sa disposition.


## Solution
On commence par décompresser le fichier zip fourni, puis nous parcourons les fichiers de l'archive dans l'objectif de comprendre comment le maître chanteur a pu voler les livres. Notre attention se porte sur le fichier `io.kubernetes.cri-o.LogPath`, qui pourrait contenir des logs qui permettraient de comprendre ce qui c'est passé. Au cours de notre exploration de ce fichier, nous tombons sur une section où des outils de piratage sont installés, à partir du github de [carlospolop](https://github.com/sponsors/carlospolop). Il semble donc que nous soyons sur la bonne piste.

<p align="center"><img src="Hacking Tools.png" alt="Hacking Tools" width="900"></p>

Nous poursuivons l'analyse des journaux pour identifier les actions réalisées par l'attaquant. Nous constatons alors qu'il a téléchargé un fichier zip depuis le serveur du CTF à l'aide de la commande suivante : `curl agent.challenges.404ctf.fr -o agent.zip`.

<p align="center"><img src="Attacker Command.png" alt="Attacker Command" width="300"></p>

Nous exécutons alors cette commande, ce qui nous permet de récupérer le fichier zip nommé `agent.zip`. Après décompression, nous découvrons à l'intérieur un fichier `flag.txt` qui contient le précieux flag.

## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{K8S_checkpoints_utile_pour_le_forensic}
```