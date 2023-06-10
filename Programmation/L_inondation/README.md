# L'Inondation

**Difficulté** : Introduction

## Enoncé

Vous prenez une collation accolé au bar du Procope, et remarquez au bout d'une dizaine de minutes un post-it, sur lequel votre nom est écrit, et en dessous une inscription : « Salut, le nouveau, viens à ma rencontre, porte de derrière ».
Curieux, vous sortez du café par cette porte et tombez nez à nez avec un jeune homme.

« Bonjour, pouquoi ce post-it ?
— Salut ! Excellente question. Dernièrement, un évènement étrange a bouleversé ma ville : elle a été prise d'une épidémie de gens se transformant en rhinocéros. Alors que ce n'était jusqu'hier qu'une dizaine de gens qui étaient touchés, j'ai vu ce matin un troupeau de ce qui semblait être plusieurs centaines de rhinocéros passer sous ma fenêtre. J'ai aussitôt saisi mon appareil photo et photographié régulièrement le troupeau pour avoir une estimation du nombre de rhinocéros, mais il y en a bien trop pour compter tout ça à moi seul ou même à deux.   
— Certes, et où voulez-vous donc en venir ?   
— Voyez-vous, j'ai entendu parler de vos talent dans les nouvelles technologies par le biais d'un ami qui fréquente ce café. J'imagine qu'un ordinateur saura compter bien plus vite que nous deux, ça vous dirait de m'aider ? D'ailleurs, on ne s'est toujours pas présentés. Moi, c'est Béranger. »

## Solution

Pour résoudre ce challenge, on se connecte au serveur à l'adresse challenges.404ctf.fr:31420. Le serveur nous envoie un message contenant une séquence de caractères représentant une des rhinocéros (i.e. la chaîne : ~c`°^). On dispose alors de quelques secondes pour compter le nombre de rhinocéros et envoyer la réponse. On doit répéter cette opération avec succès 100 fois pour obtenir le flag. Pour y parvenir, il est nécessaire d'automatiser le processus en utilisant un algorithme.


``` python
from pwn import remote

host = 'challenges.404ctf.fr'
port = 31420

def main():
    nc = remote(host, port)
    print(nc.readlineS())
    
    for k in range(100):
        res = ""
        for i in range(35):
            res+=nc.readlineS()
        print(res)
        print("round :",k)
        count_rhino = str(res.count(")"))
        print(count_rhino)
        nc.sendline(count_rhino.encode())

    for i in range(6):
        print(nc.readlineS())
main()
```


## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{4h,_l3s_P0uvo1rs_d3_l'iNforM4tiqu3!}
```
