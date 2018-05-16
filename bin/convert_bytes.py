from bin import Transposition as trans
import codecs

def convertFileToString(file):
    with open(file, "rb") as im:
        byteString = codecs.encode(im.read(), 'base64')

    plain = byteString.decode('utf-8')
    
    return plain

def convertStringToFile(string, ext):
    byteString = string.encode('utf-8')

    fh = open("output."+ext, "wb")
    fh.write(codecs.decode(byteString, 'base64'))
    fh.close()

    print("File converted")

##Testing and example of use
    
##naam en extension as variables om enige waarde te aanvaar
image = "pic.jpg"

plain = convertFileToString(image)

enc = trans.encMessage(8, plain)

with open('enc.enc', 'w') as file:
    file.write(str(enc))

dec = trans.decMessage(8, enc)

##extension moet as variable in gesit word
convertStringToFile(dec, "jpg")
