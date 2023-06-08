from chiffrement import *

def brute_force(mot):
    prev_mot = mot
    next_mot = chiffre_mot_taille_5(mot)

    while next_mot!=mot:
        prev_mot = next_mot
        next_mot = chiffre_mot_taille_5(next_mot)
        #print(next_mot)
  
    return prev_mot

# Dechiffre le mot mit en entrée
def main():
    mot = input("Entrez une mot : ")

    r = (5-len(mot)%5)%5
    mot = mot + "a"*r
    n = len(mot)
    res = ""
    for i in range(0,n,5):
        dechiffrer = brute_force(mot[i:i+5])
        res = res + dechiffrer
    print(res)

main()