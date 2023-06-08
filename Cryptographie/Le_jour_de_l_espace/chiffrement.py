vec_b1 = [9, 11, 5, 13, 19]  #Correspond au chiffré de baaaa
vec_b2 = [4, 0, 6, 14, 21]   #Correspond au chiffré de abaaa
vec_b3 = [18, 2, 7, 15, 22]  #Correspond au chiffré de aabaa
vec_b4 = [20, 1, 10, 16, 23] #Correspond au chiffré de aaaba
vec_b5 = [8, 3, 12, 17, 24]  #Correspond au chiffré de aaaab
vecteurs = [vec_b1, vec_b2, vec_b3, vec_b4, vec_b5]

# Traduire une suite de chiffres compris entre 0 et 25 en mots, en associant à chaque chiffre la lettre de l'alphabet qui à pour indice ce chiffre.
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

# Chiffre un mot, comme le fait le serveur.
# Attention ne sont chiffré que les mots écrits en minuscule, de taille 5, ne contenant pas de z
def chiffre_mot_taille_5(mot):
    alphabet = {
        'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
        'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18,
        't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24
    }

    res = [0,0,0,0,0]
    for i in range(5) :
        lettre = mot[i]
        indice = alphabet[lettre]
        vec = [k*indice for k in vecteurs[i]]
        res = [res[k]+vec[k] for k in range(5)]
    res = [k%25 for k in res]
    return traduire_en_mot(res)


def main():
    mot = input("Entrez une mot : ")
    chiffrer = chiffre_mot_taille_5(mot)
    print(chiffrer)

#main()