# Dessine-moi une courbe elliptique

## Enoncé

Au cours d'une de vos explorations dans le café, vous surprenez la conversation suivante :

Oh ! Ce jour, je m'en souviens parfaitement, comme si c'était hier. À cette époque, je passais mes journées à mon bureau chez moi, avec comme seule occupation de dessiner les illustrations qui m'étaient commandées par les journaux du coin. Je ne m'en rendais pas compte à ce moment, mais cela faisait bien 6 ans que je vivais cette vie monacale sans réelle interaction humaine. Le temps passe vite quand on n'a rien à faire de ses journées. Mais ce jour-là, c'était différent. Je m'apprêtais à commencer ma journée de travail, un peu stressé parce que j'avais des illustrations que je devais absolument finir aujourd'hui. Alors que je venais de m'installer devant ma planche à dessin, quelle ne fut pas ma surprise d'entendre une voix venir de derrière-moi :
« S'il-te plaît, dessine moi une courbe elliptique. »
Je me suis retourné immédiatement. Un petit bonhomme se tenait derrière moi, dans mon appartement, habillé de façon tout à fait incongrue. Il portait une sorte de tenue de mousquetaire céleste ? Même aujourd'hui je ne sais toujours pas comment la décrire.   
« Quoi ?   
— S'il-te plaît, dessine moi une courbe elliptique. »   
Devant cette situation ubuesque, mon cerveau a lâché, a abandonné. Je ne cherchais plus à comprendre et je me contentais de répondre:   
« Je ne sais pas ce que c'est.   
— Ce n'est pas grave, je suis sûr que tu pourras en dessiner une belle! Répondit l'enfant en rigolant. »   
Machinalement, je pris mon crayon, et je dessinai à main levée une courbe, sans réfléchir. Après quelques instants, je me suis retourné, et j'ai montré le résultat à l'enfant, qui secoua immédiatement la tête.   
« Non, regarde: cette courbe à un déterminant nul, je ne veux pas d'une courbe malade ! »   
À ce moment, je ne cherchais plus à comprendre ce qu'il se passait. J'ai donc fait la seule chose que je pouvais faire, j'en ai redessiné une. Cette fois, l'enfant était très heureux.   
« Elle est magnifique ! Je suis sûr qu'elle sera très heureuse toute seule. »   
Et là, sous mes yeux ébahis, la courbe pris vie depuis mon dessin, et s'envola dans la pièce. Elle se mit à tourner partout, avant de disparaître. J'étais bouche bée, enfin encore plus qu'avant.   
« Ah, elle avait envie de bouger visiblement !   
— Où est-elle partie ?   
— Je ne sais pas. Mais c'est toi qui l'a dessinée ! Tu ne devrais pas avoir de mal à la retrouver. En plus je crois qu'elle t'a laissé un petit souvenir, dit-il en pointant le sol, où une série de chiffres étaient effectivement dessinés sur le parquet.   
— Merci encore ! Sur ce, je dois partir. Au revoir ! »   
Avant que je puisse ouvrir la bouche, il disparût.   
Je ne sais toujours pas ce qu'il s'est passé ce jour-là, mais je retrouverais cette courbe un jour !   

## Solution

Étant donné le titre du challenge, on peut supposer que le chiffrement sera lié aux [courbes elliptiques](https://fr.wikipedia.org/wiki/Courbe_elliptique). Pour commencer, nous analysons les ressources du défi, notamment en exécutant le fichier Python à l'aide de la commande : `sage --python3 challenge.py`.

Après analyse de `challenge.py`, nous découvrons que l'algorithme de chiffrement fonctionne de la manière suivante :   
- Trois valeurs, a, b et p, sont définies.   
- Nous considérons la courbe elliptique définie par l'équation y^2 = x^3 + a*x + b modulo p.   
- Deux points aléatoires sont sélectionnés sur cette courbe, notés P1=(x1, y1) et P2=(x2, y2).   
- On affiche les valeurs de P1, P2 et p.   
- Les valeurs de a et b sont concaténées pour former une clé.   
- On définit une valeur IV et on l'affiche en hexadécimal.
- Le flag est chiffré à l'aide de l'algorithme AES qui prend en entrée la valeur de IV et la clé précédemment définie.   
- Le chiffré du flag est affiché en hexadécimal.   

Afin de déchiffrer le drapeau, nous avons besoin de la valeur de la clé. Pour obtenir cette clé, nous devons déterminer les valeurs de a et b. Pour cela, il suffit de poser un système d'équations avec les points P1 et P2, puis de le résoudre modulo p. Les méthodes pour résoudre ce système sont disponibles sur de nombreux [sites web](https://crypto.stackexchange.com/questions/97811/find-elliptic-curve-parameters-a-and-b-given-two-points-on-the-curve). Toutes les valeurs de (x1, y1), (x2, y2), p, hexa(IV), hexa(AES(flag)) se trouve dans la ressource data.txt.

Cette solution est implémentée dans `solve.py`.

## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{70u735_l35_gr4nd35_p3r50nn3s_0nt_d_@b0rd_373_d35_3nf4n7s}
```