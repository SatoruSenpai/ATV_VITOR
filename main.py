# Código da aula 01 eeee aula 04
from flask import Flask

app_vitor = Flask (__name__)
# Feature código aula 02
def saudacoes(nome):
    return f'Olá, {nome}'

# Feature código aula 03
@app_vitor.route('/rota1')
def rota1():
    return 'Olá Usuário!!'

@app_vitor.route('/rota2')
def rota2():
    resposta = "<h3> Essa é uma página da rota 2 </h3>"
    return resposta

# Feature código aula 04
@app_vitor.route("/")
def homepage():
    return("homepage.html")
@app_vitor.route("/contato")
def contato():
    return("contato.html")
# Feature código aula 02
if __name__ == "_main_":
    app_vitor.run()