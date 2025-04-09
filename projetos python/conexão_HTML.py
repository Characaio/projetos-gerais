from flask import flask,request,render_template
import sqlite3 as sql

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("Trabalho de PW customizado.html")

@app.route("/enviar",methods=["POST"])

def enviar():
    nome = request.form["nome"]
    sexo = request.form["sexo"]
    idade = request.form["idade"]
    telefone = request.form["telefone"]
    email = request.form["email"]
    
    rua = request.form["rua"]
    numero = request.form["numero"]
    cidade = request.form["cidade"]
    estado = request.form["estado"]
    periodo = request.form["periodo"]
    mensagem = request.form["mensagem"]
    senha = request.form["senha"]
    
    conn = sql.connect("teste de HTML")
    cursor = conn.cursor()
    
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS usuarios(
                       id INTEGER PRIMERAY KEY AUTOINCREMENT,
                       nome TEXT,
                       sexo TEXT,
                       idade INTEGER,
                       telefone TEXT,
                       email TEXT,
                       rua TEXT,
                       numero INTEGER,
                       cidade TEXT,
                       estado TEXT,
                       periodo TEXT,
                       mensagem TEXT,
                       senha TEXT,
                   )
                   """)
    
    cursor.execute("INSERT INTO usuarios(nome,sexo,idade,telefone,email,rua,numero,cidade,estadi,periodo,mensagem,senha) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")
    conn.commit()
    conn.close()
    return "deu tudo certo cumpade"

if __name__ == "__main__":
    app.run(debug=True)