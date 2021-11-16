
def autenticaUsuario(usuario, db):
    linha = db.select("select senha FROM tb_usuario WHERE usuario = '" + usuario['user'] + "';")
    print(linha[0])
    if str(linha[0]) == str(usuario['pass']):
        print("autenticado")
        return True
    else:
        return False


def autenticaToken(usuario, db):
    linha = db.select("select token from tb_usuario where usuario = '" + str(usuario['user']) + "';")
    if str(linha[0]) == str(usuario['token']):
        return True
    else:
        return False
