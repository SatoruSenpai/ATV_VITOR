# Código da aula 01
from flask import Flask

app_vitor = Flask (__name__)

@app_vitor.route('/')
def raiz():
    return 'Olá, turma!'

# Fea código aula 02
def saudacoes(nome):
    return f'Olá, {nome}'

# Fea código aula 03
@app_vitor.route('/rota1')
def rota1():
    return 'Olá Usuáriooo!!'
@app_vitor.route('/rota2')
def rota2():
    resposta = "<h3> Essa é uma página da rota 2 </h3>"
    return resposta
# Fea código aula 02
if __name__ == "_main_":
    app_vitor.run()