# Código da aula 01 e aula 04
from flask import Flask

app_vitor = Flask (__name__)

# Feature código aula 02 e aula 06
@app_vitor.route('/<id>')
def saudacoes(id):
    return('homepage_nome.html', nome=id)

# Feature código aula 03
@app_vitor.route('/rota1')
def rota1():
    return 'Olá Usuário!!'

@app_vitor.route('/rota2')
def rota2():
    resposta = "<h3> Essa é um página da rota 2 </h3>"
    return resposta

# Feature código aula 04
@app_vitor.route("/")
def homepage():
    return("homepage.html")

@app_vitor.route("/contato")
def contato():
    return("contato.html")

# Feature código aula 05
@app_vitor.route("/index")
def indice():
    return("index.html")

@app_vitor.route("/usuario")
def dados_usuario():
    nome_usuario="Vitor"
    dados_usuario = {"profissao":"Aluno", "disciplina":"Desenvolvimento Web III"}
    return("usuario.html", nome = nome_usuario, dados = dados_usuario)

# Feature código aula 02
if __name__ == "__main__":