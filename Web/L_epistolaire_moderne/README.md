# L'Épistolaire moderne

**Difficulté** : Moyen

## Enoncé

Une femme frôle votre table et s'éloigne avec hâte. Les effluves de son parfum vous plongent brutalement dans votre passé, faisant remonter subitement de vieux souvenirs amoureux. Les émotions surgissent et un sentiment de nostalgie et de tristesse profonde s'empare de vous.

Vous décidez d'affronter cette douleur amoureuse et d'en parler à l'une des plus grandes figures du drâme de l'amour : la Princesse de Clève. Peut-être obtiendrez vous ses conseils et secrets.

Toutes les informations nécessaires à la résolution de ce challenge sont présentes dans l'énoncé ci-dessus.

> <p align="center"> https://epistolaire.challenges.404ctf.fr/ </p>


## Solution

Pour ce challenge, nous avions accès à un chat (assez têtu) à qui nous pouvions envoyer des messages une fois connecter en tant qu'invité : 

<p align="center"><img src="Chat.png" alt="Chat princesse de cléve" width="600"></p>

On constate rapidement que les discutions avec le bot ne donne aucune informations intéraissante. Il faut donc chercher autre chose, commensont par le code source du bot. En regardant ce qu'il se passe, nous voyons qu'il y a des fichiers .js qui sont appelés : 

<p align="center"><img src="Code Chat.png" alt="Code Chat princesse de cléve" width="500"></p>

On vas directement checker le fichier main.js qui appellent surement les autres fichiers .js : 

<p align="center"><img src="Main JS.png" alt="Main JS" width="800"></p>

Il s'agit d'un code presque illisible (ou du moins incompréhensible) comme ceci. Pour y voir plus clair nous allons utiliser un site qui va nous remettre tout ce code d'aplomb : https://beautifier.io/
Avec ce site nous obtenons un code structuré avec une indentation correcte et donc lisible plus facilement. Après un survol du code, nous voyons que lorsqu'un texte est envoyé, le site va appeler une API pour donner une réponse. Cela explique donc pourquoi les réponses de la princesse étaient toujours les mêmes... En cherchant donc les principales requête HTTP d'une API (GET, POST, PUT, DELETE...) nous trouvons rapidement une fonction intéressante : 

<p align="center"><img src="Fonction API.png" alt="Fonction API" width="700"></p>

Cette fonction nous donne un indice sur le "type de texte" intéressant à envoyer : une URL.
Nous voyons également qu'il y a une fonction nommé getToken ce qui est intéressant car il y a peut être quelque chose à récupérer avec ou dans cette fonction : 

<p align="center"><img src="Get Token API.png" alt="Get Token API" width="700"></p>

Cette fonction permet de récupérer un cookie, surement celui d'un service sur le serveur ou même celui de la princesse. Si nous faisons donc un lien entre tout ce que nous avons trouvé précédemment, il nous faut un lien que nous allons envoyer à la princesse pour récupérer un token. On vas pour cela utiliser le site [Request Bin](https://public.requestbin.com/r/ent8nzdugrnzm).

En envoyant notre lien, nous récupérons directement le résultat et le fameux token, un JWT : 

<p align="center"><img src="Request Token.png" alt="Request Token" width="700"></p>

Nous récupérons ce token JWT :  
`eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwdWJsaWNfaWQiOiI3NTUwODhhMS0wNDcxLTQyYzgtYjdhZS1mNzdmZjhmN2Y3OWUiLCJleHAiOjE2ODY1MDUyNTUsImlhdCI6MTY4NjUwMzQ1NSwiaXNzIjoiaHR0cHM6Ly9lcGlzdG9sYWlyZS5jaGFsbGVuZ2VzLjQwNGN0Zi5mciJ9.L0GBPpxE_Lt9rSpfnsJbo0-GrYw1tXjgmm9lejJISiw`

On se connecte avec ce token, on a alors accès a une nouvelle page dans laquelle on trouve le flag : 

<p align="center"><img src="Token connection.png" alt="Token connection" width="700"></p>


## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{L34k_d3_C00k13s_s3cr3ts}
```
