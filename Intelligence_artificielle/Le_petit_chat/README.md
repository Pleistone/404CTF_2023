# Le Petit Chat

## Enoncé

Ebloui par les reflets du soleil sur l'imposante vitrine du café littéraire lors d'une éclaircie, vous plissez les yeux et marquez un temps d'arrêt. Une boule dorée attire votre attention. Tiens, ce n'est pas une boule, mais un petit chat orange, le regard absorbé par la vitrine luisante. Vous vous étonnez de remarquer des lunettes de soleil surplombant ses magnifiques moustaches blanches, il semble étrangement équipé en cette pluvieuse journée. Par curisosité, vous sortez du café et vous vous approchez discrètement, ayant senti votre mouvement, le chat se retourna.

« Vous ne seriez pas Hackademicien par hasard, dit-il, d'un air effrayé.   
— Non pourquoi ?   

Soulagé, le petit chat se retourna complètement, se leva de tout son long sur ses deux pattes arrières, frotta ses griffes sur son pelage et vous tendit la patte.   
— Je suis le Chat botté ! Ravi de faire votre connaissance !   

N'étant pas plus surpris de voir un chat qui parle qu'un chat avec des lunettes languissant devant un café littéraire, vous décidez de tendre votre main à votre tour.   
— Mon maître, Monsieur le Marquis de Carabas m'attend dans ce café, malheureusement, je ne peux pas le rejoindre, les chiens sont interdits.   
— Et alors ? Vous êtes un chat, vous devriez pouvoir entrer.   
— Justement, je suis censé pouvoir rentrer, mais l'intelligence artificielle qui garde l'entrée se mélange les neurones ! Voilà qu'elle confond les chiens et les chats.   
— C'est très dérangeant.   
— À cause de ce dysfonctionnement, je me retrouve dehors, dit-il, en levant ses lunettes et en vous regardant intensément avec ses gros yeux noirs et son aura envoûtante.   
— Vous allez m'aider, n'est-ce pas ?

Ne sachant que répondre face à cette claire injustice, vous décidez seulement d'acquiescer de la tête. Satisfait, le chat s'approcha et vous proposa à voix basse :   
— Vous vous y connaissez dans l'art du camouflage ? Oui ? Excellent, c'est exactement ce qu'il me faut. J'ai entendu dire que le thé était très apprécié dans cet endroit, pouvez-vous m'aider à me faire passer pour une théière ? Cela me permettrait de rejoindre mon maître ! »

Ne pouvant plus faire demi-tour, vous prenez une profonde respiration pour vous concentrer sur votre objectif : transformer ce petit chat roux en théière !

Pour valider le challenge, il faudra upload votre image de chat modifié sur internet et récupérer son URL. Enfin, il vous suffira de vous connecter via netcat et d'entrer l'URL du chat modifié. Voici un site possible : https://imgtr.ee/. L'image originale est téléchargeable ci-dessous : chat.jpg.

Vous pouvez vous aider du script verificateur.py afin d'avoir le modèle utilisé et de pouvoir essayer en local. Attention ! Ne ~modifiez~~ pas trop le petit chat, il faut que son maître puisse le reconnaître.

Un peu de lecture pour trouver l'inspiration : http://clpav.fr/lecture-chat-botte.htm. (Ne sert à rien pour résoudre le challenge)


## Solution

L'objectif de ce challenge est de modifier l'image `chat.png` de manière à ce qu'elle soit reconnue par l'algorithme `signature.py` en tant que théière, mais on doit toujours reconnaître le chat. Une fois cette modification réussie, nous téléchargeons l'image modifiée sur le site https://imgtr.ee/. Ensuite, nous envoyons l'URL au serveur en établissant une connexion avec la commande `nc challenges.404ctf.fr 32525`.

On a trois solutions pour modifier l'image :   
solution 1 : On intègre du bruit dans l'image en utilisant la technique de descente de gradient afin de faire converger le vecteur de sortie de l'image "chat" vers le vecteur de sortie de l'image "teapot" sans pour autant qu'elle soit trop modifiée. Cette solution est implémentée dans le fichier "solve1.py".

<p align="center"><img src="solution 1.png" alt="Solution 1" width="200"></p>

Solution 2 : Cette approche consiste à appliquer un watermark en forme de théière sur l'image tout en brouillant le reste de l'image. Pour ce faire, nous prenons une photo d'une théière et rapprochons autant que possible les pixels de l'image "chat.png" vers les pixels de l'image de la théière, en veillant à ne pas dépasser l'écart maximal autorisé par la vérification dans "verification.py". Cette solution est implémentée dans "solve2.py".

<p align="center"><img src="solution 2.png" alt="Solution 2" width="200"></p>

Solution 3 : Dans "verification.py", nous constatons que l'IA chargée de reconnaître une théière ou non prend en entrée une image de taille quelconque et la redimensionne en une image de taille 224*224. Cependant, le code de vérification pour s'assurer que nous n'avons pas trop modifié l'image du chat ne prend en compte que les pixels des 224 premières lignes et des 224 premières colonnes de l'image. Il suffit donc de prendre une grande image de théière, de placer l'image du chat dans le coin supérieur droit, et le tour est joué. C'est ce qui est réalisé dans "solution 3.jpg".

<p align="center"><img src="solution 3.jpg" alt="Solution 3" width="200"></p>

## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{qU3l_M4n1f1qu3_the13R3_0r4ng3}
```