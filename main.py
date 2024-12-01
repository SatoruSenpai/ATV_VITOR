# Código da aula 01
from flask import Flask

app_vitor = Flask (__name__)

@app_vitor.route('/')
def raiz():
    return 'Olá, turma!'

# fea código aula 02
def saudacoes(nome):
    return f'Olá, {nome}'
if __name__ == "_main_":
  app_vitor.run()