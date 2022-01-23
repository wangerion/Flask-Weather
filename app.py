from flask import Flask, render_template, request
import requests
from werkzeug.utils import redirect
from helpers import cityfinder


app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == 'POST':
        city = request.form.get("city")
        print(cityfinder(city))
        return render_template("showcase.html", city=cityfinder(city))
    else:
        return render_template("index.html")
