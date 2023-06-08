# À la fin de l'envoi, je signe !

## Enoncé
Alors que vous étiez entrain de vous diriger vers la sortie du café, vous entendez subitement du bruit venir d'un petit attroupement formé autour d'une table. Un homme, debout, semble visiblement agaçé par quelque chose.   
« C'est inadmissible ! Comment je peux me défendre maintenant ? Si je répond à leurs critiques, ils me traiteront de troll !   
— Calme-toi Pierre, tu sais bien que ça nous gène tout autant que toi.   
— C'est une insulte, c'est un affront, que dis-je, c'est une hérésie !   
— T'en fait toujours trop, souris celle dont vous vous souvenez qu'elle s'appelle Marthe.   
— Qu'est-ce qu'il se passe ? Demandez-vous en vous rapprochant de la conversation.   
— Salutations à vous, vous répondis Pierre en vous saluant avec son chapeau. Nous sommes dans une situation terrible ! Nous possédions un système de signature très avancé au sein du groupe qui nous permettait de signer des messages au noms du groupe. Malheureusement, l'ancien administrateur du système est parti, et nous n'avons plus le contrôle dessus. J'ai l'habitude de me défende contre toute sorte de viles critiques quant aux ouvrages que je produis, mais maintenant que je ne peux plus signer mes réponses, je vais perdre toute crédibilité ! Pauvre de moi !   
— Je peux essayer de regarder ce système si vous voulez.   
— Vous pensez pouvoir reprendre la main dessus ? Si vous y arriviez, vous aurez ma reconnaissance éternelle !   
— Ça vaut le coup d'essayer ! Répondez vous en souriant, amusé par la grandiloquence du bonhomme. »   


## Solution

Le fichier "signature.py" contient l'algorithme appliqué par le serveur, auquel on peut accéder en utilisant la commande nc challenges.404ctf.fr 30724.
En analysant ce fichier, nous découvrons les éléments suivants :
- Pour obtenir le flag, il faut envoyer un JSON. Ce JSON a un champ "data" qui contient un texte commençant par "gimme flagz", et un champ "sign" qui contient la signature de ce qui est contenu dans "data".
- La signature d'un texte se fait en plusieurs étapes. Tout d'abord, le texte est converti en binaire. Ensuite, le binaire est découpé en 66 blocs. Enfin, chaque bloc est signé. Pour signer un bloc, on applique le hachage MD5 sur la clé privée autant de fois que la valeur du bloc. Par exemple, si le bloc est égal à 11 en binaire, ce qui correspond à la valeur décimale 3, on applique 3 fois le hachage MD5 sur la clé privée.

On peut alors remarquer qu'il y a une faiblesse dans ce type de signature. En effet si on posséde une paire message_1/signature_1 valide, on peut signer n'importe quel autre message dont les blocs ont tous des valeurs supérieures aux blocs de message_1. Pour crée cette nouvelle signature il suffit de réappliquer le hachage MD5 sur signature_1 autant de fois que nécessaire pour atteindre la valeur du bloc de notre nouveau message.

C'est précisément ce qui est implémenté dans le fichier "solve.py".


## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{Wint3r_i5_c0m1ng}
```