import os
import numpy as np
class VernamCipher:
    text = ""
    key = ""
    cipherText = ""

    def __init__(self):
        print("Object not defined, please insert args")


    def __init__(self, text):
        self.key = VernamCipher.generateKey()
        self.text = text
        # VernamCipher.giveVernam(self, text, key)

    def __init__(self, text, key):
        self.text = text
        self.key = key
        # VernamCipher.giveVernam(self, text, key)


    def giveVernam(self, text, key):
        i = 0

        for char in text:
            # cipherText = self.cipherText
            self.cipherText += chr(ord(char) ^ ord(key[i]))
            i += 1
            # print(self.cipherText)
            if i == len(key):
                i = 0
        return self.cipherText

    def generateKey(self):
        file = open("key.txt", "w")
        key = str(np.random.randint(low=1000000, high=100000000))
        # print(key)
        file.write(key)
        file.close()
        print("key generated")

    def toString(self):
        print("Plaintext: " + self.text + "\nKey: " + self.key +
              "\nciphertext: " + self.cipherText)

    def decryptVern(self, ciphertext, key):
        self.cipherText=""
        return VernamCipher.giveVernam(self, text=ciphertext, key=key)

def main():
    plaintext = input("insert plaintext: ")
    ciphertext = ""
    choice = input("own or random key? o/r: ")
    key = ""
    if choice == "o":
        key = input("insert own key: ")
        vernobj = VernamCipher(plaintext, key)
        ciphertext = vernobj.giveVernam(plaintext, key)
        vernobj.toString()
        print("\nCiphertext decrypted: " + vernobj.decryptVern(ciphertext, key))

    else:
        vernobj = VernamCipher(text=plaintext)
        file = open("key.txt", "r")
        key = file.readline()
        file.close()
        ciphertext = vernobj.giveVernam(text=plaintext, key=key)
        vernobj.toString()
        print("\nCiphertext decrypted: " + vernobj.decryptVern(ciphertext, key))