#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

/* Renvoie d'une manière ressemblant à de l'aléatoire un chiffre compris entre 0 et param_1.
La suite de nombres renvoyés est entièrement déterminée lors de l'initialisation à l'apelle de  : srand(time(NULL)) */
int pseudo_random_number(int param_1){
  int iVar1;
  do {
    iVar1 = rand();
    iVar1 = iVar1 / (int)(0x7fffffff / (long)(param_1 + 1));
  } while (param_1 < iVar1);
  return iVar1;
}

/* Renvoie aléatoirement un caractère dans la chaîne de caractère a0 */
char *random_char(char *a0){
    int n = strlen(a0) - 1;
    int random = pseudo_random_number(n);
    return a0[random];
}

/*Genere le mot de passe valide pour le programme "cache_cache_le_retour" */
void get_mdp(){
  char* char_list[4];
  char_list[0] = "1234567890";
  char_list[1] = "abcdefghijklmnoqprstuvwyzx";
  char_list[2] = "ABCDEFGHIJKLMNOPQRSTUYWVZX";
  char_list[3] = "!@#$%^&*(){}[]:<>?,./";
  int char_list_number = 4;

  char mdp[20];
  char *rand_char;
  int rand_int;
  srand(time(NULL));
  for (int i=20; i != 0; i = i-1) {
    rand_int = pseudo_random_number(char_list_number-1);
    rand_char = random_char(char_list[rand_int]);
    strncat(&mdp,&rand_char,1);
  }

  printf("%s\n", &mdp);
}

int main() {
    /*Permet d'ajuster le ping avec le serveur*/
    sleep(0.2);
    /*Pour avoir le mot de passe valide il faut lancer à la même second la communication avec "nc challenges.404ctf.fr 31725" et ce programme*/
    get_mdp();

    

}


/*
int FUN_00101243(void)

{
  __pid_t _Var1;
  int iVar2;
  size_t sVar3;
  int uVar4;
  long in_FS_OFFSET;
  int local_4b8;
  int local_4b4;
  char *local_4b0;
  size_t local_4a8;
  char *local_4a0;
  char *local_498;
  void *local_490;
  FILE *local_488;
  FILE *local_480;
  __ssize_t local_478;
  char *local_470;
  char *local_468;
  char *local_460;
  undefined8 local_458;
  char local_448 [48];
  char local_418 [1032];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  fgets(local_448,0x28,stdin);
  local_4a0 = "mystere.zip";
  local_498 = "surprise.txt";
  local_4b8 = 0;
  fgets(local_418,0x400,stdin);
  sVar3 = strcspn(local_418,"\n");
  local_418[sVar3] = '\0';
  remove(local_4a0);
  remove(local_498);
  local_490 = (void *)FUN_0010110a(local_418,&local_4b8);
  local_488 = fopen(local_4a0,"wb");
  if (local_488 == (FILE *)0x0) {
    puts(&DAT_00101878);    Echec le fichier mystere.zip doit etre présent
    free(local_490);
    local_490 = (void *)0x0;
    uVar4 = 1;
  }
  else {
    fwrite(local_490,1,(long)local_4b8,local_488);
    fclose(local_488);
    local_488 = (FILE *)0x0;
    _Var1 = fork();
    if (_Var1 == 0) {
      local_4b4 = open("/dev/null",1);
      if (local_4b4 < 0) {
        exit(1);
      }
      iVar2 = fileno(stdout);
      dup2(local_4b4,iVar2);
      iVar2 = fileno(stderr);
      dup2(local_4b4,iVar2);
      close(local_4b4);
      local_470 = "unzip";
      local_468 = "unzip";
      local_460 = "mystere.zip";
      local_458 = 0;
      execvp("unzip",&local_468);
      exit(0);
    }
    wait((void *)0x0);
    local_480 = fopen(local_498,"r");
    if (local_480 == (FILE *)0x0) {
      puts(&DAT_00101878);   Echec le fichier surprise.txt doit etre présent
      free(local_490);
      local_490 = (void *)0x0;
      uVar4 = 1;
    }
    else {
      local_4b0 = (char *)0x0;
      local_4a8 = 0;
      local_478 = getline(&local_4b0,&local_4a8,local_480);
      if (local_478 == -1) {
        puts(&DAT_00101878); chec le fichier surprise.txt doit etre présent
        uVar4 = 1;
      }
      else {
        puts(local_4b0);
        remove(local_4a0);
        remove(local_498);
        fclose(local_488);
        fclose(local_480);
        free(local_4b0);
        free(local_490);
        local_490 = (void *)0x0;
        local_488 = (FILE *)0x0;
        local_480 = (FILE *)0x0;
        local_4b0 = (char *)0x0;
        uVar4 = 0;
      }
    }
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
    __stack_chk_fail();
  }
  return uVar4;
}


void * FUN_0010110a(char *param_1,int *param_2)

{
  int iVar1;
  size_t __size;
  void *__s;
  BIO_METHOD *type;
  BIO *pBVar2;
  BIO *append;
  
  __size = strlen(param_1);
  __s = malloc(__size);
  memset(__s,0,__size);
  *param_2 = 0;
  type = BIO_f_base64();
  pBVar2 = BIO_new(type);
  BIO_set_flags(pBVar2,0x100);
  append = BIO_new_mem_buf(param_1,(int)__size);
  pBVar2 = BIO_push(pBVar2,append);
  iVar1 = BIO_read(pBVar2,__s,(int)__size);
  *param_2 = iVar1;
  BIO_free_all(pBVar2);
  return __s;
}

*/