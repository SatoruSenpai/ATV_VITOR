from flask import Flask

app_vitor = Flask(__name__)

# Função para renderizar a tela de login
@app_vitor.route('/')
def login():
    return('login.html')

# Rota para tratar o login (validação da senha)
@app_vitor.route('/entrar', methods=['POST'])
def entrar():
    username = request.form.get('username')
    password = request.form.get('password')

    # Aqui você pode colocar sua lógica para validar o login (no exemplo, são simples)
    if username == "Vitor" and password == "saopaulo123":
        return "Login bem-sucedido!"
    else:
        return "Usuário ou senha incorretos. Tente novamente."

# Rota para a página de criação de login (registro)
@app_vitor.route('/criar_login')
def criar_login():
    return "Página de criação de login (registrar usuário)"

if __name__ == '__main__':
    app_vitor.run()