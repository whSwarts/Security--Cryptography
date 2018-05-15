import math

#decryption method
def decMessage(key, cText):
    #caluculate amount of columns
    columns = int(math.ceil(len(cText) / key))
    #define an array with num of columns
    mess = [''] * columns
    #number of spaces in array
    boxes = columns * key

    shaded = boxes - len(cText)
    col = 0
    row = 0

    for char in cText:
        mess[col] += char
        col += 1

        if (col == columns) or (col == columns - 1 and row >= key - shaded):
            col = 0
            row += 1
            
    return ''.join(mess)

#encryption method
def encMessage(key, mess):
    cText = [''] * key
    
