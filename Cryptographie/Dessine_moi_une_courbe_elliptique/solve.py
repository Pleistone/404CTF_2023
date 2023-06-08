from Crypto.Cipher import AES
import hashlib

# Cherche l'inverse modulaire de a modulo n. C'est-à-dire le nombre b tel que a*b congrue à 1 modulo n.
def inverse_modulaire(a, n):
    # Appliquer l'algorithme d'Euclide étendu
    r, r_prev = n, a
    s, s_prev = 0, 1

    while r != 0:
        quotient = r_prev // r
        r, r_prev = r_prev - quotient * r, r
        s, s_prev = s_prev - quotient * s, s

    # Vérifier si l'inverse modulaire existe
    if r_prev != 1:
        raise ValueError("L'inverse modulaire n'existe pas.")
    
    # Normaliser l'inverse modulaire dans l'intervalle [0, n-1]
    inverse = s_prev % n
    return inverse

# Détermine l'équation d'une courbe elliptique de la forme y^2 = x^3 + a*x +b
def get_AES_key(x1,y1,x2,y2,p):
    r1 = (y1**2-y2**2)%p
    r2 = (x1**3-x2**3)%p
    r3 = (r1-r2)%p

    d = (x1-x2)%p
    i = inverse_modulaire(d, p)
    a = (r3*i)%p
    print("a =",a)

    r1 = (y2**2-x2**3)%p
    r2 = (a*x2)%p
    b = (r1-r2)%p
    print("b =",b)

    key = str(a) + str(b)
    print("key =",key)
    return key


# Déchiffre AES
def decrypt_aes(key, iv, cipher):
    aes = AES.new(hashlib.sha1(key.encode()).digest()[:16], AES.MODE_CBC, iv=iv)
    deciphered = aes.decrypt(cipher)
    return deciphered


# On détermine la clé à partir de 2 points de la courbe elliptique.
x1 = 93808707311515764328749048019429156823177018815962831703088729905542530725
y1 = 144188081159786866301184058966215079553216226588404139826447829786378964579

x2 = 139273587750511132949199077353388298279458715287916158719683257616077625421
y2 = 30737261732951428402751520492138972590770609126561688808936331585804316784 

p = 231933770389389338159753408142515592951889415487365399671635245679612352781
key = get_AES_key(x1,y1,x2,y2,p)

# On convertit le iv en bytes
iv_hex = "00b7822a196b00795078b69fcd91280d"
iv = bytes.fromhex(iv_hex)
print("iv =",iv)

# On convertit le texte chiffré en bytes
cipher_hex = "8233d04a29befd2efb932b4dbac8d41869e13ecba7e5f13d48128ddd74ea0c7085b4ff402326870313e2f1dfbc9de3f96225ffbe58a87e687665b7d45a41ac22"
cipher = bytes.fromhex(cipher_hex)

# On déchiffre le texte
deciphered = decrypt_aes(key, iv, cipher)
print(deciphered)
