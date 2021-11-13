from flask import Flask, render_template, request, url_for,redirect, jsonify
from extesions.DataBase import *
from extesions.Token import *
from extesions.Autentica import *
from config import *


app = Flask(__name__)
db = DataBase(CONFIG)
# API DE LOGIN
@app.route("/login", methods=['POST'])
def login():
    usuario = request.get_json()
    if autenticaUsuario(usuario, db):
        token = toToken(usuario, CONFIG)
        db.update("UPDATE tb_usuario SET token = " + str(token)+ "WHERE usuario = " + usuario['user'])
        return jsonify({'sucess': True, 'token': token})
    else:
        return jsonify({'sucess': False})

# API PARA RECUPERAR AS FECHADURAS DE UMA CONTA
@app.route("/listaFechadura", methods=['POST'])
def listaFechadura():
    usuario = request.get_json()
    usuario = toText(usuario)
    if autenticaToken(usuario, db):
        lista = listaFechadura(usuario,db)
        return jsonify({'sucess': True, 'fechaduras' : lista})
    else:
        return jsonify({'sucess': False})

# API PARA CADASTRAR UM NOVO USUARIO
@app.route("/cadastro", methods=['POST'])
def listaFechadura():
    usuario = request.get_json()
    #implementar
    

@app.route("/abreFechadura", methods=['POST'])
def abreFechadura():
    usuario = request.get_json()
    usuario = toText(usuario)
    if autenticaToken(usuario, db):
        #implementar
        return jsonify({'sucess': True})
    else:
        return jsonify({'sucess': False})


@app.route("/fechaFechadura", methods=['POST'])
def fechaFechadura():
    usuario = request.get_json()
    usuario = toText(usuario)
    if autenticaToken(usuario, db):
        #implementar
        return jsonify({'sucess': True})
    else:
        return jsonify({'sucess': False})


@app.route("/notificacao", methods=['POST'])
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
    


    




