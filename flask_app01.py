from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Cia yra home page su Flask</h1>"

@app.route("/orai")
def orai():
    return "Orai yra per karsti"

@app.route("/<kintamasis>")# cia adreso juosta
def user(kintamasis):# cia sujungia su adresu
    return f"<h1>Sveiki {kintamasis} atvyke i flask puslapi</h1>"



if __name__ == "__main__":
    app.run()
