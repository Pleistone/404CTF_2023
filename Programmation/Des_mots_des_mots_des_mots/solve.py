from pwn import remote
from rules import rules
import re

host = 'challenges.404ctf.fr'
port = 30980

def main():

    list_taille = [4,3,5,9,10]
    list_mot = ["cosette","ettesoc","ttsoc","ottsc","PPtt!15QRUWcos"]
    nc = remote(host, port)

    for k in range(5):
        for i in range(list_taille[k]):
            print(nc.readlineS())
        nc.sendline(list_mot[k].encode())
        print(list_mot[k])

    texte=""
    for i in range(3):
        texte+=nc.readlineS()
    print(texte)

    mots_entre_accolades = re.findall(r'{(.*?)}', texte)
    liste_mot= mots_entre_accolades[0].split()
    traduction = rules(liste_mot)
    nc.sendline(traduction.encode())
    print(traduction)
    print(nc.readlineS())
    print(nc.readlineS())

main()