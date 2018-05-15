import math

def decMessage(key, cText):
    
    columns = int(math.ceil(len(cText) / key))
    mess = [''] * columns
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

def encMessage(key, mess):
    cText = [''] * key

    for column in range(key):
        pointer = column

        while pointer < len(mess):
            cText[column] += mess[pointer]
            pointer += key
    return ''.join(cText)
