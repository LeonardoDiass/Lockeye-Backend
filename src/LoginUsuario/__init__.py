from flask import Flask, render_template, request, jsonify
import requests
from uuid import uuid4
from flask_cors import CORS
import json
from DataBase import DataBase
from Token import *
from config import *

app = Flask(__name__)
CORS(app)

db = DataBase(DATABASE)

def autentica(usuario, senha):
    senha_db = db.select(f"select senha from tb_usuario where usuario = {usuario}")
    if senha_db == senha:
        return True
    else:
        False

def token(usuario, key):
    valor = toToken(usuario, key)
    return jsonify({'sucesso': 'true', 'token': valor})


@app.route("/login", methods = ['POST'])
def login():
    data = request.get_json()
    usuario = data["usuario"]
    senha = data["senha"]
    if autentica(usuario,senha):
        return token(usuario, CHAVE_API)
    else:
        return jsonify({'sucesso': 'false', 'token': 'null'})
 

if __name__ == "__main__":
    app.run()