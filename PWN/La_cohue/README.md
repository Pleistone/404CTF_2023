# La Cohue

**Difficulté** : Facile

## Enoncé

Le café littéraire est plongé dans une agitation frénétique. Un petit boule jaune virevolte dans tous les sens, semant la panique parmi les clients. Au milieu du chaos, une silhouette se détache, immobile et imperturbable : c'est Francis Jammes. Vous vous frayez difficilement un chemin à travers la foule jusqu'à lui. Il vous explique alors qu'il vient d'adopter un canari un peu excentrique, qui s'est échappé de sa cage et qui semble avoir élu domicile dans le café. Francis vous lance un regard légèrement inquiet et vous demande si vous pourriez l'aider à retrouver son volatile farceur. Alors que vous vous apprêtiez à partir, James vous murmure à l'oreille : « Sachez que parfois, un canari peut en cacher un autre » .

Que décidez-vous de faire ?

Toutes les informations nécéssaires à la résolution de ce challenge sont présentes après s'être connecté en netcat.


## Solution

On commence par exécuter le fichier pour observer le comportement du programme :

<p align="center"><img src="Execution du programme.png" alt="Execution du programme" width="400"></p>

Après avoir testé les différentes fonctionnalités, on passe à une analyse plus approfondie en décompilant le programme "la_cohue" avec Ghidra. En regardant la liste des fonctions on remaque une fonction `canary()` qui permet d'afficher le flag :

```c
void canary(void){
  FILE *__stream;
  long in_FS_OFFSET;
  char flag [72];
  long canary;

  canary = *(long *)(in_FS_OFFSET + 0x28);
  puts(&DAT_00400b98);
  __stream = fopen("flag.txt","r");
  fgets(flag,0x48,__stream);
  puts(flag);
  fclose(__stream);
  if (canary != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}
```

Y a plus qu'à trouver un moyen l'appeler. On a un `printf` vulnérable dans l'option `2` du programme : 
```c
fgets(user_says,0x40,stdin);
...
printf(user_says);
...
```

Qui va-nous permettre de faire fuiter la stack, par exemple mettant en entrée la chaîne de caractère `%17$p` on récupère la position du canary dans la stack. Puis avec l'option `1` une autre vulnérabilité va nous permettre d'écrire sur la stack, pour écraser l'adresse de retour de la fonction par l'adresse de la fonction `canary()`.

```c
fgets(user_says,0x40,stdin);
gets(user_says);
```

On code appliquant cela est implémenté dans `solve.py`.


## Flag

<details>
<summary> Flag 🚩</summary>

```
404CTF{135_C4N4r15_41M3N7_14_C0MP46N13_N3_135_141553Z_P45_53U15}
```