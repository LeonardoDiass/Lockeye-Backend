from flask import Flask, render_template, request, url_for,redirect, jsonify
from flask_cors import CORS, cross_origin
from extesions.DataBase import *
from extesions.Token import *
from extesions.Autentica import *
from extesions.ListaFechadura import *
from config import *


app = Flask(__name__)
db = DataBase(CONFIG)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


# API DE LOGIN
@app.route("/login", methods=['POST'])
@cross_origin()
def login():
    usuario = request.get_json()
    if autenticaUsuario(usuario, db):
        token = toToken(usuario, CONFIG)
        db.update("update tb_usuario set token = '" + str(token)+ "' where usuario = '" + usuario['user'] + "';")
        return jsonify({'sucess': True, 'token': str(token)})
    else:
        return jsonify({'sucess': False})


# API PARA RECUPERAR AS FECHADURAS DE UMA CONTA
@app.route("/listaFechadura", methods=['POST'])
@cross_origin()
def listaFechadura():
    usuario = request.get_json()
    print(usuario)
    usuario = toText(usuario, CONFIG)
    if autenticaToken(usuario, db):
        lista = listarFechadura(usuario,db)
        return jsonify({'sucess': True, 'fechaduras' : lista})
    else:
        return jsonify({'sucess': False})


# API PARA CADASTRAR UM NOVO USUARIO
@app.route("/cadastrar", methods=['POST'])
def cadastrar():
    usuario = request.get_json()
    #implementar
    

@app.route("/abrirFechadura", methods=['POST'])
@cross_origin()
def abreFechadura():
    usuario = request.get_json()
    codigo = usuario['codigo']
    usuario = toText(usuario, CONFIG)
    if autenticaToken(usuario, db):
        db.update("update tb_fechadura set status1 = 'aberto' where codigo = " + str(codigo) + ";")
        return jsonify({'sucess': True})
    else:
        return jsonify({'sucess': False})


@app.route("/fecharFechadura", methods=['POST'])
@cross_origin()
def fechaFechadura():
    usuario = request.get_json()
    codigo = usuario['codigo']
    usuario = toText(usuario, CONFIG)
    if autenticaToken(usuario, db):
        db.update("update tb_fechadura set status1 = 'fechado' where codigo = " + str(codigo) + ";")
        return jsonify({'sucess': True})
    else:
        return jsonify({'sucess': False})


@app.route("/notificacar", methods=['POST'])
def notificacao():
    usuario = request.get_json()
    usuario = toText(usuario)
    if autenticaToken(usuario, db):
        #implementar
        return jsonify({'sucess': True})
    else:
        return jsonify({'sucess': False})


if __name__ == "__main__":
    app.run()
    


    





