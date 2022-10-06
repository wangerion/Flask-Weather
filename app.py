from flask import Flask, flash, render_template, request
import os
import requests
from werkzeug.utils import redirect
from helpers import cityfinder


app = Flask(__name__)

SECRET_KEY = os.environ.get("SECRET_KEY")

app.secret_key = SECRET_KEY

units = {
    '˚C, m/s': 'metric',
    '˚F, mph': 'imperial'
}


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == 'POST':
        city = request.form.get("city")
        temp = units.get(request.form.get("tempvalues"))
        print(temp)
        print(cityfinder(city, temp))
        if not cityfinder(city, temp):
            flash("Unable to search for that city. Try again!", category='error')
            return render_template("index.html", units=units)
        return render_template("show_weather.html", city=cityfinder(city, temp), units=units)
    else:
        return render_template("index.html", units=units)
