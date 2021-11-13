
def autenticaUsuario(usuario, db):
    linha = db.select("SELECT senha FROM tb_usuario WHERE usuario = " + usuario['user'])
    if linha[0] == str(usuario['pass']):
        return True
    else:
        return False


def autenticaToken(usuario, db):
    linha = db.select("SELECT token FROM tb_usuario WHERE usuario = " + usuario['user'])
    if linha[0] == str(usuario['token']):
        return True
    else:
        return False
