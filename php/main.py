from flask import Flask

app = Flask(__name__)

#rotas
@app.route("/")
def homepage():
    return "Olá Mundo!!!"

if __name__ == "__main__":
    app.run()