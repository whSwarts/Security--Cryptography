import numpy as np
from Transposition import Transposition
from Vigenere import Vigenere
from Vernam import Vernam

key = "123abc"
plaintext = "Hello world!"

def encrypt(msg, key):
    vernOb = Vernam.VernamCipher(msg, key)
    vernem = vernOb.giveVernam(msg, key)

    k = 0
    for char in key:
        k += ord(char)
    np.random.seed(k)

    msgNum = []
    for char in vernem:
        msgNum.append(ord(char))
    print(msgNum)
    np.random.shuffle(msgNum)
    print(msgNum)
    cipher = ""
    for i in range(0, len(msgNum)):
        cipher += chr(msgNum[i]+k)
    print(cipher)
    return cipher

def decrypt(cipher, key):
    vernOb = Vernam.VernamCipher(cipher, key)
    vernem = vernOb.giveVernam(cipher, key)
    k = 0
    for char in key:
        k += ord(char)
    np.random.seed(k)

    ciphNum = []
    for char in cipher:
        ciphNum.append(ord(char))
    print(ciphNum)
    np.random.shuffle(ciphNum)
    print(ciphNum)
    cipher = ""
    for i in range(0, len(ciphNum)):
        cipher += chr(ciphNum[i] - k)
    print(cipher)

cipher = encrypt(plaintext, key)
decrypt(cipher, key)