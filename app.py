from flask import Flask, render_template

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

if __name__ == '__main__':
    app.run()