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



def cadastrar(usuario, senha):
    try:
        db.insert(f"INSERT INTO tb_usuario(usuario,senha) VALUES({usuario},{senha})")
    except:
        return False

@app.route("/login", methods = ['POST'])
def login():
    data = request.get_json()
    usuario = data["usuario"]
    senha = data["senha"]
    if cadastrar(usuario,senha):
        return jsonify({'sucesso': 'true'})
    else:
        return jsonify({'sucesso': 'false'})
 

if __name__ == "__main__":
    app.run()