from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/compras')
def compras():
    return render_template('compras.html', item1 = "Farinha", item2 = "Cuscuz")

@app.route('/mercado')
def mercado():
    return render_template('mercado.html')

@app.route('/gastos', defaults = {"mes":"Janeiro", "valor":"None"})
@app.route('/gastos/<mes>/<valor>')
def gastos(mes, valor):
    return render_template('gastos.html', a=mes, b=valor)

@app.route('/dobro', defaults = {"n": 1})
@app.route('/dobro/<float:n>')
@app.route('/dobro/<int:n>')
def dobro(n):
    resul = n*2
    return render_template('dobro.html', n = n, result = resul)

@app.route('/dados')
def dados():
    return render_template('dados.html')

@app.route('/recebedados', methods = ['POST'])
def recebedados():
    nome = request.form['nome']
    email = request.form['email']
    estado = request.form['estado']
    # request.args para recuperar os dados via método GET
    return render_template('recebedados.html', n = nome, e = email, es = estado)

@app.route('/verificação/<int:idade>')
def verificacao(idade):
    if idade >= 18:
        return "Você é MAIOR de idade"
    else:
        return "Você é MENOR de idade"
    
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/verificalogin', methods=['POST'])
def verificalogin():
    usuario = request.form['usuário']
    senha = request.form['senha']
    if usuario == "Alba" and senha == "123":
        return render_template('verificalogin.html', u = usuario)
    else:
        return "Você não tem permissão"

@app.route('/verificaidade2/<int:idade>')
def verificaidade2(idade):
    return render_template('verificaidade2.html', i = idade)

@app.route('/usuario/<nome>')
def usuario(nome):
    return render_template('usuario.html', n = nome)

if __name__ == '__main__':
    app.run()