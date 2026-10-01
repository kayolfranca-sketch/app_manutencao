from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import csv
import os
from datetime import datetime
app = Flask(__name__)
PASTA_PROJETO = os.path.dirname(os.path.abspath(__file__))
ARQUIVO = os.path.join( PASTA_PROJETO, "solicitacoes.csv")
CAMPOS = [
"id",
"nome",
"tipo_usuario",
"sala",
"equipamento",
"descricao",
"data",
"status"
]
