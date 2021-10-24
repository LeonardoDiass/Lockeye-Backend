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

def listarFechaduras(usuario, senha):
    fechaduras = db.select(f"select codigo from tb_pertence where usuario = {usuario}")
    dic = {}
    for i in fechaduras:
        pass
    return fechaduras
    
@app.route("/lista", methods = ['POST'])
def login():
    data = request.get_json()
    usuario = toText(data['token'])
    fechaduraras = listarFechaduras(usuario)
    
 

if __name__ == "__main__":
    app.run()