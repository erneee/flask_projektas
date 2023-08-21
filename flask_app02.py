from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/orai")
def orai():
    return render_template("orai.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("forma.html")
    if request.method == 'POST':
        vardas = request.form['vardas']
        return render_template("vardas.html", sablono_kint=vardas)

@app.route("/<kintamasis>")
def user(kintamasis):
    return render_template("vardas.html", sablono_kint=kintamasis)


@app.route("/ciklas")
def ciklas():
    return render_template("ciklas.html")


if __name__ == "__main__":
    app.run()
