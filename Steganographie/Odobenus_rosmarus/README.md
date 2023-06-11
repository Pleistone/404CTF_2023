# Odobenus Rosmarus

**Difficulté** : Introduction

## Enoncé

« Bonjour à toi, et bienvenue au café littéraire ! »

Connais-tu la première règle de la lecture ? Ne pas s'attacher aux mots. Il faut les surpasser, chercher l'idée derrière. L'existence précède l'essence, ici nous cherchons l'essence des choses, et non pas leur existence ou leur forme.

Je te laisse un petit quelque chose. Prouve moi que tu peux lire entre les lignes.

> Ce soir je Célèbre Le Concert Electro Comme Louis Et Lou. Comme La nuit Commence Et Continue Clairement, Et Clignote Lascivement il Chasse sans Chausser En Clapant Encore Classiquement Les Cerclages du Clergé. Encore Car Encore, Louis Lou Entamant Longuement La Lullabile En Commençant Le Cercle Exhaltant de Club Comique Cannais Et Clermontois.

> Format : 404CTF{cequevousalleztrouver}


## Solution

Le challenge porte le nom d'Odobenus Rosmarus, qui est le nom d'une espèce de morse. De plus, dans le texte fourni dans l'énoncé, on peut remarquer de nombreux mots commençant par une majuscule. Ces lettres initiales sont toujours un C, un L ou un E, ce qui pourrait correspondre aux signaux Morse pour Court, Long et Espace, les trois caractères utilisés dans le code Morse. En mettant bout à bout ces caractères, on obtient la séquence suivante : CCLCECLELCLCECCECLCCECECLCCECELLELLLECLCECCCEC. On la traduit et on trouve le flag.

<p align="center"><img src="Code morse.jpg" alt="Code morse" width="500"></p>


## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{FACILELEMORSE}
```
