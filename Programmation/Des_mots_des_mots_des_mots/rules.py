from collections import Counter

def split_texte(texte):
    mots = texte.split()
    return mots

#Inverser mot
def rule_1(mot):
    mot_inverse = mot[::-1]
    return mot_inverse

#Appliquer regles mot
def rule_2(mot):
    longueur_mot = len(mot)
    moitie = longueur_mot // 2
    if longueur_mot % 2 == 0:
        mot_inverse = mot[moitie:] + mot[:moitie]
        return mot_inverse
    else:
        mot_sans_centrale = mot.replace(mot[moitie], "")
        return mot_sans_centrale

#Décale les voyelles
def rule_3(mot, mot_modif):
    consonnes = "bcdfghjklmnpqrstvwxz"
    
    if len(mot) < 3:
        return mot
    
    if mot_modif[2] in consonnes:
        mot = decalage_voyelles_gauche(mot)
    else:
        mot = decalage_voyelles_droite(mot)
    
    mot = rule_1(mot)
    mot = rule_2(mot)
    return mot

#Décale les voyelles vers la gauche
def decalage_voyelles_gauche(mot):
    voyelles = "aeiouy"
    prev_voyelle = ""
    first_indice = 0

    mot_list = list(mot)
    mot = ""

    for indice, lettre in enumerate(reversed(mot_list)):
        if lettre in voyelles:
            if prev_voyelle=="":
                prev_voyelle = lettre
                first_indice = len(mot_list)-indice-1
                mot = lettre + mot
            else:
                mot = prev_voyelle + mot
                prev_voyelle = lettre
        else :
            mot = lettre + mot

    mot_list = list(mot)
    mot_list[first_indice]=prev_voyelle
    return "".join(mot_list)

#Décale les voyelles vers la droite
def decalage_voyelles_droite(mot):
    mot_list = list(mot)
    voyelles = "aeiouy"
    prev_voyelle = ""
    first_indice = 0

    for indice, lettre in enumerate(mot_list):
  
        if lettre in voyelles:
            if prev_voyelle=="":
                prev_voyelle = lettre
                first_indice = indice
            else:
                temp = mot_list[indice]
                mot_list[indice] = prev_voyelle
                prev_voyelle = temp

    mot_list[first_indice]=prev_voyelle
    return "".join(mot_list)



#Modifie les caratére ascii seulon un certain calcule puis tri les lettre du mot
def rule_4(mot):
    mot = ascii_transforme(mot)
    mot = tri_mot(mot)
    return mot


def ascii_transforme(mot):
    mot_list = list(mot)
    consonnes = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
    voyelles = "aeiouyAEIOUY"

    dictionnaire = {'b': ord('a'), 'B': ord('A'), 'c': ord('a'), 'C': ord('A'), 'd': ord('a'), 'D': ord('A'), 'f': ord('e'), 'F': ord('E'), 'g': ord('e'), 'G': ord('E'),
                    'h': ord('e'), 'H': ord('E'), 'j': ord('i'), 'J': ord('I'), 'k': ord('i'), 'K': ord('I'), 'l': ord('i'), 'L': ord('I'), 'm': ord('i'), 'M': ord('I'),
                    'n': ord('i'), 'N': ord('I'), 'p': ord('o'), 'P': ord('O'), 'q': ord('o'), 'Q': ord('O'), 'r': ord('o'), 'R': ord('O'), 's': ord('o'), 'S': ord('O'),
                    't': ord('o'), 'T': ord('O'), 'v': ord('u'), 'V': ord('U'), 'w': ord('u'), 'W': ord('U'), 'x': ord('u'), 'X': ord('U'), 'z': ord('y'), 'Z': ord('Y')}

    for indice, lettre in enumerate(mot_list):
        if lettre in consonnes:
            vp = dictionnaire[lettre]
            som = 0
            for i in range(indice):
                som += ord(mot_list[i])*(2**(indice-i))*(mot_list[i] in voyelles)
            ascii = ((vp+som)%95)+32
            mot_list.insert(indice+1,chr(ascii))

    mot = "".join(mot_list)
    return mot

def tri_mot(mot):
    # Compter le nombre d'occurrences de chaque caractère dans le mot
    occurrences = Counter(mot)
    # Trier les caractères en utilisant les critères spécifiés
    resultat = sorted(occurrences.keys(), key=lambda c: (-occurrences[c], ord(c)))
    # Construire le mot trié en conservant le bon nombre d'occurrences pour chaque lettre
    mot_trie = ''.join(c * occurrences[c] for c in resultat)
    return mot_trie



def rules(liste_mot):
    res = ""
    for mot in liste_mot:
        mot_modif = rule_1(mot)
        mot_modif = rule_2(mot_modif)
        mot = rule_3(mot,mot_modif)
        mot = rule_4(mot)
        res+=mot+" "
    return res[:-1]

