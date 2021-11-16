
def listarFechadura(usuario,db):
    lista = []
    codigo = db.select("select codigo_fechadura from tb_pertence where dono = '" + str(usuario['user']) + "';")
    for i in codigo:
        linha = db.select("select * from tb_fechadura where codigo = " + str(i) + ";")
        lista.append(linha)
    print(lista)
    return lista