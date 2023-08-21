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

@app.route("/naujienos")
def ciklas():
    return render_template("naujienos.html")





if __name__ == "__main__":
    app.run()


# Flask užduotis
# 1. Sukurti endpointą /naujienos, jam šabloną su su tekstu "Čia mano puslapio naujienos"
# 2. Sukurti nuorodas visuose šablonuose, kad būtų galima atsivertus bet kokį puslapį,
# patekti į pradinį puslapį, orų, logino, naujienų puslapius. Visas nuorodas sudėti į pastraipas (<p>) tegas.
# 3. Sukurti naują endpointą /pasisveikink5, jame turėtų būti forma, įvedus į ją
# tekstą, pvz vardą, atsidarytų kitas puslapis(šablonas) su pasisveikinimu 5 kartus.