#Cópdigo da aula 01
from flask import Flask
app_vitor = Flask (__name__)
@app_vitor.route('/')
def raiz():
    return 'Olá, turma!'
app_vitor.run()