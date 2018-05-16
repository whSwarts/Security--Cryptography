import math

#decryption method
def decMessage(key, cText):

    if(key > len(cText)):
        key = round(len(cText) - (len(cText)/2))

    #caluculate amount of columns
    columns = int(math.ceil(len(cText) / key))
    #define an array with num of columns
    mess = [''] * columns
    #number of spaces in array
    boxes = columns * key
    #calculate how many spaces in the array will have no values
    shaded = boxes - len(cText)
    col = 0
    row = 0
    #loop through each character in cipher text
    for char in cText:
        #add character to array and increment the value of the column
        mess[col] += char
        col += 1
        #if the end of the row is reached, restart column at 0 and increment row
        #this also occurs if a shaded space is reached
        if (col == columns) or (col == columns - 1 and row >= key - shaded):
            col = 0
            row += 1
    #join array into a single string            
    return ''.join(mess)

#encryption method
def encMessage(key, mess):
    if (key > len(mess)):
        key = round(len(mess) - (len(mess) / 2))
    #define an array so that there is a column per charcter in key
    cText = [''] * key
    #Define key index
    cIndex = 0
    #Convert message to string
    mess = str(mess)
    #Define length of message
    length = len(mess)
    #Start looping through each character in message
    for sym in mess:
        #Add character to array
        cText[cIndex] += sym
        #Increment key index and revert it to zero if key value is reached
        cIndex += 1
        if cIndex == key:
            cIndex = 0
    #join array into a single string, printing per column  
    return ''.join(cText)

