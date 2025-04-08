import pandas as pd
from flask import Flask, jsonify

tabela_rol_procedimentos = pd.read_csv('tabela_estruturada.csv')
app = Flask(__name__)

@app.route('/')
def index():
    tabela_dict = tabela_rol_procedimentos.to_dict()
    return jsonify(tabela_dict)
    
@app.route('/procedimentos')
def get_procedimentos():
    procedimentos = tabela_rol_procedimentos["PROCEDIMENTO"].to_dict()
    procedimentos_json = jsonify(procedimentos)
    
    return procedimentos_json

@app.route('/subgrupos')
def get_subgrupos():
    subgrupos = tabela_rol_procedimentos["SUBGRUPO"].to_list()
    subgrupos_distintos = list(set(subgrupos))
    
    d = {}
    for k, v in enumerate(subgrupos_distintos):
        d[k] = v
    
    return jsonify(d)

@app.route('/vigencias')
def get_vigencias():
    vigencias = tabela_rol_procedimentos["VIGÊNCIA"].to_list()
    vigencias_distintas = list(set(vigencias))
    
    d = {}
    for k, v in enumerate(vigencias_distintas):
        d[k] = v
    
    return jsonify(d)

@app.route('/grupos')
def get_grupos():
    grupos = tabela_rol_procedimentos["GRUPO"].to_list()
    grupos_distintos = list(set(grupos))
    
    d = {}
    for k, v in enumerate(grupos_distintos):
        d[k] = v
    
    return jsonify(d)

@app.route('/capitulos')
def get_capitulos():
    capitulos = tabela_rol_procedimentos["CAPÍTULO"].to_list()
    capitulos_distintos = list(set(capitulos))
    
    d = {}
    for k, v in enumerate(capitulos_distintos):
        d[k] = v
    
    return jsonify(d)


