# La Quête du sens [3/3]

**Difficulté** : Moyen

## Enoncé

Maintenant Marceline veut monter son propre journal, qu'elle nommera en l'honneur de ce café : Le Procope Littéraire ! Elle pense demander à ses amis Alphonse, François-René, Alfred et Alfred d'écrire des articles. Cependant, ils ne semblent pas inspirés. Pour créer, il leur faut un lieu à la fois sublime et ténébreux ! Ils leur faut revenir aux origines, en somme. Voici ce qui ressort de leur conversation par message :

François-René : il me semble que les catacombes de Paris seraient sources d'une inspiration ténébreuse.

Alfred : en effet

Alphonse : mais que serait le sublime sans nature ?

Alfred : en effet

Marceline : dis-donc, les deux Alfred, vous ne voudriez pas expliciter un peu plus vos noms ? Cette conversation me donne mal à la tête

Alfred : ...

Alfred : je viens de me souvenir d'un lieu originel qui pourrait retracer avec superbe nos pas dans le romantisme sans ignorer ni les ténèbres ni le sublime.

Alphonse : un lac ?

François-René : un cimetière ?

Marceline : toujours aussi proche de la mort mon cher François-René.

Marceline : pourquoi une formulation aussi alambiquée ? Précise ta pensée Alfred

Alfred : mais je n'ai rien dit moi

Alphonse : ...

Marceline : ...

François-René : ...

Retrouvez le lieu ainsi que son propriétaire, bien connu des deux Alfred.   
> Format : 404CTF{numero_adresse_rue_prenom_nom_du_proprietaire}   
> exemple : 404CTF{36_quai_des_orfevres_jean_dupont}


## Solution

On commence par chercher quels est le nom complet des deux Alfred, on liste donc les différentes personnalités nommées Alfred qui ont vécu à cette époque :   
- Alfred De Vigny (1797 - 1863)   
- Alfred de Musset (1810 - 1857)   
- Alfred de Bougy (1814 - 1871)   
- Alfred Des Essarts (1811 - 1893)   
- Alfred de Bréhat (1822 - 1866)   
- Alfred Jarry (1873 - 1907)

En regardant un peu plus en detail la vie de chacun d'eux on vois que Alfred De Vigny et Alfred de Musset  se connaisent. De plus la période sur la quel ils ont vécus correspond a la période sur la quels ils on vécu correspond à celle des autre participant (Marceline Desbordes-Valmore, François René de Chateaubriand et Alphonse de Lamartine). 

On cherche donc un lieu qui est connu des deux Alfred. De plus, ils mentionnent un "lieu originel", ce qui suggère qu'il s'agit probablement d'un endroit qu'ils ont fréquenté dans leur jeunesse. En consultant Wikipédia, on découvre qu'ils ont tous deux participé au Cénacle, qui se tenait à la Bibliothèque de l'Arsenal sous la direction de Charles Nodier. Ce bâtiment se trouve aux 1-3 rue de Sully.


## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{3_rue_de_sully_charles_nodier}
```