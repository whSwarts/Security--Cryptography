VIGENERE_TABLE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encryptMess(key, message):
    return messTranslation(key, message, 'enc')

def decryptMess(key, message):
    return messTranslation(key, message, 'dec')

def messTranslation(key, message, func):
    #storage for dec/enc message
    translation = []

    keyIndex = 0
    key = key.upper()
    message = message.upper()

    for sym in message:
        index = VIGENERE_TABLE.find(sym)

        #check that symbol is in VIGENERE_TABLE
        if index != -1:
            
            #enc/dec message
            if func == 'enc':
                index += VIGENERE_TABLE.find(key[keyIndex])
            elif func == 'dec':
                index -= VIGENERE_TABLE.find(key[keyIndex])

            #handle the wrap-around for both positive and negative
            index %= len(VIGENERE_TABLE)

            translation.append(VIGENERE_TABLE[index])

            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translation.append(sym)
    return ''.join(translation)
