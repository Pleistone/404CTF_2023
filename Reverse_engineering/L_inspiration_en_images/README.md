# L'Inspiration en images

**Difficulté** : Facile

## Enoncé

Un quart d'heure plus tôt dans la soirée, vous étiez en train de parler avec Sabine de vos méthodes créatives, de vos exercices de style dans vos mediums respectifs. Elle mentionna au fil de la conversation son atelier de peinture se situant dans les combles rustiques du café littéraire, vous suggérant que vous pourriez toujours prendre de l'inspiration en observant ses peintures, son processus de création, sa manière de capturer la beauté insaisissable.

Une fois la conversation et le café terminés, vous vous aventurez dans l'atelier de peinture de Sabine, votre lampe torche à la main. Au milieu de cette mer de tableaux, vous repérez une peinture étrange, criblée d'inscriptions.

Et au pied du chevalet a chu une note, sur laquelle il est marqué : 'Ma clé est la couleur du fond de la toile'. Vous remarquez également d'autres inscriptions incompréhensibles au verso de la note. Sans doute un message chiffré ?

Vous vous mettez en quête de la clé.

Note : Le déchiffrage du message n'est pas nécessaire à la complétion du challenge.

> Format : 404CTF{vec4(r,g,b,a)} où r,g,b et a sont des flottants précis au dixième.


## Solution

On décompile le fichier `vue_sur_un_etrange_tableau` avec Ghidra. On commence ensuite par analyser la fonction main.

<p align="center"><img src="Analyse du main.png" alt="Analyse du main" width="800"></p>

Après une analyse rapide de la fonction main, on repère une instruction qui ressemble fortement à ce qui nous intéresse : `(*glad_glClearColor)(0x3e4ccccd,0x3e99999a,0x3e99999a,0x3f800000)`. En effet, il s'agit d'un vecteur au format (r,g,b,a) avec des valeurs correspondant à des nombres flottants. On utilise alors un [site en ligne](https://resource.heltec.cn/utils/hf) pour convertir ces nombres en flottant, et on obtient les valeurs suivantes : 0.2, 0.3, 0.3 et 1.0.

## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{vec4(0.2,0.3,0.3,1.0)}
```
