from flask import Flask, render_template, request, redirect

lista = []

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('Home.html', Titulo='Home')

@app.route('/importancia')
def importancia():
    return render_template('Importancia.html', Titulo='Importância')

@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html', Titulo='Cadastro de Pacientes')

@app.route('/exibir')
def exibir():
    return render_template('ExibirPacientes.html', Titulo='Exibir Pacientes Cadastrados', lista=lista)

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    idade = request.form['idade']
    genero = request.form['genero']
    dataCons = request.form['dataCons']
    paciente = [nome, idade, genero, dataCons]
    lista.append(paciente)
    return redirect('/exibir')

if __name__ == '__main__':
    app.run()
