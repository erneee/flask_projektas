from flask import Flask, render_template, request
import requests
import json
import sys


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

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
def naujienos():
    return render_template("naujienos.html")

@app.route('/pasisveikink5', methods=['GET', 'POST'])
def pasisveikink5():
    if request.method == 'GET':
        return render_template("pasisveikink5.html")
    if request.method == 'POST':
        vardas = request.form.get('vardas')
    return render_template('pasisveikink5.html', vardas=vardas)


# API_KEY = ""
# def gauti_oru_prognoze(API_KEY):
#     base_url = 'http://api.weatherapi.com/v1/forecast.json'
#     city = "Vilnius"
#     params = {
#         'key': API_KEY,
#         'q': 'Vilnius',
#         'days': 1,
#         'aqi': 'no',
#         'alerts': 'no'
#     }
#
#
#     headers = {
#         "Connection": "keep-alive",
#         "Vary": "Accept-Encoding",
#         "Content-Length": "2334",
#         "Content-Type": "text/html",
#         "Date": "Mon, 21 Aug 2023 08:38:51 GMT"
#     }
#
#
#
#
#     response = requests.get(base_url, params=params, headers=headers)
#     data = response.json()
#     if response.status_code == 200:
#         data = response.json()
#         print(data)
#     else:
#         print('Request failed with status code:', response.status_code)
#
#
#
#
#
#
# @app.route("/orai")
# def orai():
#     temperatura = gauti_oru_prognoze(API_KEY)
#     if temperatura is not None:
#         return render_template('orai.html', temperatura=temperatura)
#     else:
#         return "Nepavyko gauti orų prognozės."


if __name__ == "__main__":
    app.run()


# Flask užduotis
# 1. Sukurti endpointą /naujienos, jam šabloną su su tekstu "Čia mano puslapio naujienos"
# 2. Sukurti nuorodas visuose šablonuose, kad būtų galima atsivertus bet kokį puslapį,
# patekti į pradinį puslapį, orų, logino, naujienų puslapius. Visas nuorodas sudėti į pastraipas (<p>) tegas.
# 3. Sukurti naują endpointą /pasisveikink5, jame turėtų būti forma, įvedus į ją
# tekstą, pvz vardą, atsidarytų kitas puslapis(šablonas) su pasisveikinimu 5 kartus.