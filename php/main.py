from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="172.22.14.144", port=5000, debug=True)
