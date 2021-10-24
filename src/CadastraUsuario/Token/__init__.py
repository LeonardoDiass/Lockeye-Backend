def toToken(texto, key):
    #string --> bytes
    mBytes = texto.encode("utf-8")
    #bytes --> int
    mInt = int.from_bytes(mBytes, byteorder="big")
    return mInt * key

def toText(token, key):
    token = token/key
    #int --> bytes
    mBytes = token.to_bytes(((token.bit_length() + 7) // 8), byteorder="big")
    #bytes --> string     
    return mBytes.decode("utf-8")
