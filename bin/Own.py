from bin import Transposition, Vernam

key = "123abc"
plaintext = "hello world"


def encrypt(msg, key):
    k=0
    for char in key:
        k += ord(char)
    if(k >= len(msg)):
        k = len(msg) -1
    vernOb = Vernam.VernamCipher(msg, key)
    vernem = vernOb.giveVernam(msg, key)
    msgNum = []
    for char in vernem:
        msgNum.append(ord(char))
    cipher = ""
    for i in range(0, len(msgNum)):
        cipher += chr(msgNum[i]+k)
    cipher = Transposition.encMessage(k, cipher)
    return cipher


def decrypt(cipher, key):
    k = 0
    for char in key:
        k += ord(char)
    if(k >= len(cipher)):
        k = len(cipher) -1

    msgNum = []
    message = ""
    cipher = Transposition.decMessage(k, cipher)
    for char in cipher:
        msgNum.append(ord(char))

    for i in range(0, len(msgNum)):
        message += chr(msgNum[i] - k)

    msgNum.clear()
    for char in message:
        msgNum.append(ord(char))
    message = ""
    for i in range(0, len(msgNum)):
        message += chr(msgNum[i])
    vernOb = Vernam.VernamCipher(message, key)
    vernem = vernOb.decryptVern(message, key)
    return vernem

cipher = encrypt(plaintext, key)
print(decrypt(cipher, key))