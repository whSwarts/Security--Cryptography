from PIL import Image
import numpy as np
import Vigenere as vig
import Transposition as trans

def convertImageToString(img):
    mess = ""
    arr = np.array(img, dtype=np.int).flatten()
    
    for i in arr:
        mess += str(i) + " "

    return mess

def convertStringToImage(string):
    arr = np.fromstring(string, dtype=int, sep=' ')
    decArr = np.reshape(arr,(512, 512, 3))
    rescaled = (255.0 / decArr.max() * (decArr - decArr.min())).astype(np.uint8)
    
    return rescaled

## Test Code, Use in gui
## Also in GUI: Check for file extension and use as file extension for decryption
##              Check for width and height of image to use in decrypted format

im = Image.open('image.jpg')
text = convertImageToString(im)

enc = vig.encryptMess("atl034", text)

with open('enc.txt', 'w') as file:
    file.write(enc)

dec = vig.decryptMess("atl034", enc)

arr = convertStringToImage(dec)

im = Image.fromarray(arr)
im.save('out.jpg')
im.show()
