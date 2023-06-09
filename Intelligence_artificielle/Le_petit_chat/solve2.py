# Python 3.11.3
from math import floor, ceil
import numpy as np
from PIL import Image


def ajouter_bruit_image(image_entree, image_bruit, facteur):
    # Redimensionnement de l'image de bruit pour avoir les mêmes dimensions que l'image d'entrée
    image_bruit = image_bruit.resize(image_entree.size)

    # Conversion des images en tableaux numpy
    entree_array = np.array(image_entree)
    bruit_array = np.array(image_bruit)

    # Ajout du bruit à l'image d'entrée
    image_bruitee = np.clip(entree_array + facteur * bruit_array, 0, 255).astype(np.uint8)

    # Création de l'objet Image à partir du tableau numpy
    image_bruitee = Image.fromarray(image_bruitee)

    return image_bruitee


# Calcule la distance entre a et b avec la norme L2
def distance_L2(a, b):
    return np.linalg.norm(np.array(a) - np.array(b))

#Renvoie une approximation du vecteur v, qui minimise la distance avec v2,
#tel que la distance entre v et v1 soit inférieur à la distance eps
def approx_minimise_distance(v1,v2,e):
    v = []
    d = distance_L2(v1,v2)
    x = e/d

    for i in range(3):
        res = (1-x)*v1[i]+x*v2[i]
        v.append([floor(res), ceil(res)])

    min_dis = d
    min_vec = v1
    for i in v[0]:
        for j in v[1]:
            for k in v[2]:
                vec= (i,j,k)
                if distance_L2(vec,v1)<=e and distance_L2(vec,v2)<min_dis:
                    min_dis = distance_L2(vec,v2)
                    min_vec = vec
    return min_vec


def ajuster_image(image_bruitee, image_originale, eps):
    # Conversion des images en tableaux numpy
    taille = image_originale.size

    # Calcul de la distance entre les pixels et ajustement si nécessaire
    for x in range(taille[0]):
        for y in range(taille[1]):
            px_org = image_originale.getpixel((x, y))
            px_brt = image_bruitee.getpixel((x, y))
            if distance_L2(px_org, px_brt) > eps:
                new_px = approx_minimise_distance(px_org, px_brt, eps)
                image_bruitee.putpixel((x, y), new_px)

    return image_bruitee



def add_image_noise(img_entree, img_bruit):
    # Chargement de l'image d'entrée
    image_entree = Image.open(img_entree)

    # Chargement de l'image de bruit
    image_bruit = Image.open(img_bruit)

    # Facteur de bruit
    facteur = 0.95  # Ajustez ce facteur selon le niveau de bruit souhaité

    # Ajout du bruit à l'image d'entrée
    image_bruitee = ajouter_bruit_image(image_entree, image_bruit, facteur)

    # Ajustement de l'image bruitée
    eps = 70
    image_bruitee = ajuster_image(image_bruit, image_entree, eps)

    # Enregistrement de l'image modifiée
    output_file = "solution 2.png"
    image_bruitee.save(output_file, format="png")


img_entree = "chat.jpg"
img_bruit = "teapot.jpg"
add_image_noise(img_entree, img_bruit)
print("L'image modifiée a été enregistrée avec succès.")

#404CTF{qU3l_M4n1f1qu3_the13R3_0r4ng3}





