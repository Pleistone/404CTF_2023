# De la poésie

## Enoncé

Debout dans l'allée, un homme singulier regarde fixement l'imposante horloge qui, d'un vert canard, plonge la rangée de livres dans une ambiance bucolique très agréable. Perturbé par cette étrange figure, vous n'avez même pas remarqué que quelqu'un s'était rapproché de vous.

« Ne faites pas attention à lui, dit la figure à moitié cachée par l'ombre d'une rangée de livres. Il cherche de l'inspiration pour son nouveau poème, et depuis quelque temps, il est fasciné par les chiffres. Je ne sais pas ce qu'il a fait, mais cela lui a complètement retourné le cerveau, il est devenu incompréhensible. »

La voix féminine laissa place à une grande dame à lunette ronde, elle tenait en main un livre fraichement imprimé.
« Vous le connaissez ?
— Bien sûr ! Nous nous échangeons nos poèmes pour les commenter et les améliorer, mais ces dernières semaines il ne me parle presque plus, et je ne comprends rien du tout à ce qu'il m'a donné ! Regardez ça. »

Elle vous tendit le livre pour que vous puissiez l'examiner. La couverture est toute simple, il y a seulement marqué le titre : Être pair ou ne pas l'être.

Cependant, en l'ouvrant, vous vous rendez compte que ce n'est pas un livre, mais une collection d'images ! Christelle remarqua votre mine stupéfaite et ajouta :

« C'est ce que je vous disais, ce n'est pas de la poésie à ce que je sache. »

D'abord étonné, vous devenez curieux et pensif, qu'est-ce que cela peut-il bien-être ? Après quelques secondes passées à feuilleter l'ouvrage, vous vous exclamez :

«Bien sûr !   
— Comment ça ? Vous avez une idée de ce que cela peut être ?   
— Je pense oui, je crois bien pouvoir le déchiffrer. »   

 
## Solution

Le challenge nous fournit un fichier poeme.zip contenant 6535 images en noir et blanc, sur lesquelles est écrit un chiffre. L'idée est de créer un algorithme de reconnaissance d'image qui va déterminer le chiffre sur chaque image. Une fois cela réalisé, la phrase dans l'énoncé "Être pair ou ne pas l'être" suggère que l'on doit convertir cette longue chaîne de chiffres en binaire, en associant un 0 aux nombres pairs et un 1 aux nombres impairs. On obtient ainsi une longue séquence binaire que l'on convertit en texte. Cela nous donne un poème avec le flag à la fin. 

Cette solution est implémentée dans "solve.py". Après exécution, on obtient le texte suivant :  
>Et2e pair ou ne paS lettre  
>  
>Lâhomme, dont la vie entiÃ¨re  
>Est de 96 ans,  
>Dort le 1/3 de sa carriÃ¨re,  
>Ã'est juste 32 ans.Ajoutons pour maladies,  
>Procès, voyages, accidents  
>Au moins 1/4 de la vie  
>  
>C'ast0encore 2 foi3 12 ans.  
>Par!jour 2 heuRes d'études  
>Ou de travaux - foNt 8 ans,  
>Noirs chagrins, inquiétudes  
>Pour le double vont 16 ans.Pour affaires qu'on projette  
>1/2-heure, - encobe 2 aîs.  
>5/4 d'heures de toilette  
>Barbe et caetera - 7 ans.  
>Par jour pour manger et boire  
>2 font bien 8 ans.  
>Cela porte le mémoire  
>Jusqu'à 95 ans.Rdste encorm 1 an pour faire  
>Ce qu'oiseaux font au printemps.  
>Par jour l'homme a donc sur terre  
>1/4 d'heure de bon temps.  
>Juste assez pour déposE2 le drapeau sur le 424CTF :   
>404CTF{d3_L4_p03S1e_qU3lqU3_P3u_C0nT3mpkr4in3}  
>poème original : Le quast d'heure de bon temps Nicolas Boileau$  
  
Il y a quelques petits ratés du a des erreurs dans la reconnaissance des chiffres, mais on a globalement un texte lisible.
On a également quelques erreurs dans le flag que l'on vas corriger à la main.

## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{d3_L4_p03S1e_qU3lqU3_P3u_C0nT3mp0r4in3}
```

