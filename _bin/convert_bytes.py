import codecs

def convertFileToString(file):
    with open(file, "rb") as im:
        byteString = codecs.encode(im.read(), 'base64')

    plain = byteString.decode('utf-8')
    
    return plain

def convertStringToFile(string, ext, path):
    byteString = string.encode('utf-8')

    fh = open(path+"_decrypted."+ext, "wb")
    fh.write(codecs.decode(byteString, 'base64'))
    fh.close()

    print("File converted")
