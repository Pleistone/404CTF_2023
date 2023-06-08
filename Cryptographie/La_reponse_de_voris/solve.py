#!/usr/bin/python3
import numpy as np

def gen_ligne(i,n):
    ligne = []
    for k in range(n):
        if k<i:
            ligne.append(k+1)
        else:
            ligne.append(i+1)
    return ligne

def gen_matrice(n):
    matrice = []
    ligne = []
    for i in range(n-1,-1,-1):
        ligne = gen_ligne(i,n)
        matrice.append(ligne)
    return np.array(matrice)

def traduire_en_mot(suite_chiffres):
    alphabet = {
        0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i",
        9: "j", 10: "k", 11: "l", 12: "m", 13: "n", 14: "o", 15: "p", 16: "q",
        17: "r", 18: "s", 19: "t", 20: "u", 21: "v", 22: "w", 23: "x", 24: "y",
        25: "z"
    }
    
    resultat = ""
    for chiffre in suite_chiffres:
            lettre = alphabet[chiffre]
            resultat += lettre

    return resultat


# Génération de la matrice
base_matrice = gen_matrice(31)

# Inversion de la matrice
matrice_inverse = np.linalg.inv(base_matrice)

# Déchiffrement
cipherArray = np.array([[15, 21, 5, 3, 7, 19, 20, 22, 6, 1, 15, 23, 5, 7, 14, 2, 8, 3, 16, 2, 25, 13, 20, 15, 0, 12, 25, 18, 4, 25, 15]])
initial_value = np.array([[6, 21, 18, 7, 13, 12, 8, 9, 3, 22, 0, 11, 0, 1, 11, 6, 6, 12, 4, 9, 8, 16, 21, 17, 7, 10, 8, 23, 7, 13, 18]])
uncipherArray = np.dot(cipherArray-initial_value, matrice_inverse)
uncipherArray = [int(c%26) for c in uncipherArray[0]]

flag = traduire_en_mot(uncipherArray)
print(flag)
