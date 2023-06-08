#!/usr/bin/python3
# usage : sage -python3 solve3.py
from sage.all import Matrix, vector, Integers

ALPHABET = "abcdefghijklmnopqrstuvwxy"
CIPHER = "ueomaspblbppadgidtfn"
TEXT = ""
F = Integers(25)
M = Matrix(F,[[9,4,18,20,8],[11,0,2,1,3],[5,6,7,10,12],[13,14,15,16,17],[19,21,22,23,24]])

# 1. Inversion de la matrice
I = M.inverse()

#2. Dechiffement
cipherArray = []
buffer = []
for i in range(0, len(CIPHER)):
    buffer.append(ALPHABET.index(CIPHER[i]))
    if len(buffer) == 5:
        cipherArray.append(buffer)
        buffer =[]

textArray = []
for c in cipherArray:
    textArray.append(I*vector(c))

for t in textArray:
    for l in t:
        TEXT += ALPHABET[l]

print(TEXT)
# il faut enlever le dernier 'a' qui est du au padding