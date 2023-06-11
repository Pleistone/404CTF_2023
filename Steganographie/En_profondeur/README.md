# En Profondeur

**Difficulté** : Moyen

## Enoncé

Alors que vous dégustiez une assiette d'oeufs mayo, un homme fait son apparition dans Le Procope. Il prend place à côté de vous et se présente comme étant Monsieur de Valmont. Il vous raconte avoir reçu une lettre étonnante de Madame de Merteuil. Après quelques temps passé à discuter, il vous confie que celle-ci avait accepté un rendez-vous avec lui suite à un pari gagné. Il doutait franchement qu'elle honore sa parole, d'autant qu'elle voyage beaucoup et qu'il n'a pas le permis b lui permettant de la rejoindre n'importe où. Il s'interroge néanmoins sur cette lettre. Pouvez-vous aider de Valmont à voir le message caché derrière celle-ci ?

> Format : 404CTF{message_caché_chaque_mot_en_minuscule}


## Solution

On nous donne le texte suivant :

<p align="center"><img src="Ressource challenge.png" alt="Ressource challenge" width="500"></p>

Le principe utilisé repose sur les [autostéréogrammes](https://fr.wikipedia.org/wiki/Autost%C3%A9r%C3%A9ogramme). Le créateur du challenge a donc appliqué ce principe au texte (stéréogramme ASCII). L'objectif est de superposer le texte de droite et de gauche, puis d'observer les mots/lettres qui se détachent. En effet, dans les deux textes, les espaces ne sont pas exactement au même endroit. Ainsi, on peut identifier des zones où le texte se retrouve superposé à un espace de l'autre côté, rendant les mots lisibles. Ces mots lisibles forment le drapeau recherché.


## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{paris_finlande_15_6_avion}
```


