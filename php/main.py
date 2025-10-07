from flask import Flask

app = Flask(__name__)

from views import *                                         #Importa todas as rotas de Views

if __name__ == "__main__":
    app.run(host="172.22.14.144", port=5000, debug=True)
