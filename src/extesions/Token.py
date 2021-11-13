
def toToken(usuario, CONFIG):
    token = number(usuario['user']) * CONFIG['API_KEY']
    return token

def toText(usuario, CONFIG):
    usuario = user(usuario["token"], CONFIG)
    return usuario
   

def number(texto):
    #string --> bytes
    mBytes = texto.encode("utf-8")
    #bytes --> int
    mInt = int.from_bytes(mBytes, byteorder="big")
    return mInt

def user(token, CONFIG):
    user = {}
    texto = token/CONFIG['API_KEY']
    #int --> bytes
    mBytes = texto.to_bytes(((texto.bit_length() + 7) // 8), byteorder="big")
    #bytes --> string     
    user['user'] = mBytes.decode("utf-8")
    user['token'] = token
    return user