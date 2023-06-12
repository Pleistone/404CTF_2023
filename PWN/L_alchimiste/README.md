# L’Alchimiste

**Difficulté** : Facile

## Enoncé

Alors que vous vous apprêtez à quitter le café littéraire, vous êtes attiré par une lumière étrange venant d'un coin de la pièce. Vous vous approchez et apercevez une pierre rougeoyante, posée sur un vieux manuscrit portant l'inscription 'Abraham le Juif'. Un homme étrange, vêtu d'une longue cape noire, est debout à côté de la pierre, les yeux fixés dessus.

Vous essayez de saluer l'homme, mais il ne semble pas vous remarquer. Vous lui demandez ce que cette pierre intriguante représente. L'homme lève enfin les yeux vers vous et répond d'une voix grave et rauque : « ma plus belle création, la pierre philosophale ». La pierre et l'aura mystique qui l'entoure vous fascinent.

L'homme se présente alors comme Nicolas Flamel, un célèbre alchimiste du XIVe siècle. Il engage la conversation avec vous et vous initie aux mystères de l'alchimie, vous expliquant la signification symbolique de la pierre philosophale et les pouvoirs qu'on lui prête.

Vous apprenez que Flamel a passé des années à la recherche de la pierre philosophale et qu'il a finalement réussi à la créer. Ses connaissances et son enthousiasme pour cette discipline mystique vous émerveillent.

Finalement, Flamel vous donne l'adresse d'un cabinet d'alchimie secret, connu seulement des initiés, où vous pourrez en apprendre davantage sur les secrets de l'alchimie. Vous le remerciez et quittez le café, le désir d'en savoir plus sur l'alchimie vous animant.

Vous avez maintenant la possibilité de vous rendre à ce fameux cabinet d'alchimie.

Toutes les informations nécéssaires à la résolution de ce challenge sont présentes après s'être connecté en netcat.


## Solution

On commence par exécuter le fichier pour observer le comportement du programme :

<p align="center"><img src="Execution du programme.png" alt="Execution du programme" width="700"></p>

Après avoir testé les différentes fonctionnalités, on passe à une analyse plus approfondie en décompilant le programme "l_alchimiste" avec Ghidra. On commence ensuite par analyser la fonction main :

<p align="center"><img src="Main function.png" alt="Main function" width="300"></p>

On y retrouve les différentes fonctions que l'on a pu appeler lors de l'exécution du programme. On va donc analyser le fonctionnement de ces fonctions, en commençant par `view_flag()`, qui devrait être la fonction qui renvoie le flag.
```c
void view_flag(int *param_1) {
  FILE *__stream;
  char *pcVar1;
  long in_FS_OFFSET;
  char local_58 [72];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  if ((*param_1 < 0x96) || (param_1[1] < 0x96)) {
    puts(&DAT_00400f28);
  }
  else {
    __stream = fopen("flag.txt","r");
    if (__stream == (FILE *)0x0) {
                    /* WARNING: Subroutine does not return */
      exit(0);
    }
    pcVar1 = fgets(local_58,0x40,__stream);
    if (pcVar1 != (char *)0x0) {
      puts(&DAT_00400f68);
      puts("-----------------------------------------------");
      puts(local_58);
      puts("-----------------------------------------------");
                    /* WARNING: Subroutine does not return */
      exit(0);
    }
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}
```

On vois donc que pour avoir le flag il faut que la valeur de `*param_1` ou `param_1[1]` soit supérieur à 150. En allant dans le programme `createCharacter` on voit que ces valeurs correspondent à notre force et à notre intelligence, 2 valeurs qui sont initialisées à respectivement 100 et 50 au début du programme.

```c
undefined4 * createCharacter(undefined4 param_1,undefined4 param_2,undefined4 param_3) {
  undefined4 *puVar1;
  
  puVar1 = (undefined4 *)malloc(0x18);
  *puVar1 = param_1;
  puVar1[1] = param_2;
  puVar1[2] = param_3;
  *(undefined8 *)(puVar1 + 4) = 0;
  return puVar1;
}
```

Il faut donc trouver un moyen d'augmenter notre force ou notre intelligence à plus de 150. On analyse alors les autres fonctions.

Tout d'abord, on peut acheter un élixir :
```c
void buyStrUpPotion(long joueur){
  long *elixir;

  puts(&DAT_00400dc8);
  elixir = (long *)malloc(0x48);
  printf("***** ~ %p\n",elixir);
  *elixir = 0x6420726978696c45;
  elixir[1] = 0x6563726f662065;
  elixir[8] = (long)incStr;
  if (*(int *)(joueur + 8) < 0x32) {
    puts(&DAT_00400df8);
  }
  else {
    *(long **)(joueur + 0x10) = elixir;
    *(int *)(joueur + 8) = *(int *)(joueur + 8) + -0x32;
  }
  return;
}
```

Si on a assez d'argent, un pointeur vers "l'élixir" est ajouté dans la structure `joueur`.

Ensuite on peut appeler la fonction `useItem()` pour consommer cet élixir :

```c
void useItem(long joueur){
  if (*(long *)(joueur + 0x10) == 0) {
    puts(&DAT_00400e38);
  }
  else {
    puts(&DAT_00400e7f);
    puts("***** Vous sentez votre force augmenter.");
    (**(code **)(*(long *)(joueur + 0x10) + 0x40))(joueur);
    printf("***** ~ %p\n",*(undefined8 *)(joueur + 0x10));
    free(*(void **)(joueur + 0x10));
  }
  return;
}
```

Elle vérifie qu'on a bien un élixir (ie le pointeur précédent), à la fin le `free()` libère l'emplacement mémoire utilisé par l'élixir, mais ne le remet pas à null, il est donc toujours présent dans la structure `joueur`.

Problème, si on consomme à nouveau un élixir, on a un double free et le programme crash.

En revanche, on peut appeler `sendMessage()`

```c
void sendMessage(void){
  void *__buf;

  __buf = malloc(0x48);
  printf("\n[Vous] : ");
  read(0,__buf,0x48);
  printf("***** ~ %p\n",__buf);
  return;
}
```

Qui alloue aussi une zone mémoire pour recevoir notre message, comme la zone précédemment utilisée pour l'élixir est considérée comme libre, elle va être utilisée.

On fait ça 5 fois de suite et on augmente les points de FORCE.

Si ont veut augmenter l'intelligence, l'idée est la même, mais en plus on va écraser le pointeur vers `incStr()` par l'adresse de `incInt()`

On code appliquant cela est implémenté dans `solve.py`.


## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{P0UrQU01_P4Y3r_QU4ND_135_M075_5UFF153N7}
```
