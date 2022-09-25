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
        temp = request.form.get("tempvalues")
        print(temp)
        print(cityfinder(city))
        if not cityfinder(city):
            flash("Unable to search for that city. Try again!", category='error')
            return render_template("index.html", units=units)
        return render_template("index.html", city=cityfinder(city), units=units)
    else:
        return render_template("index.html", units=units)
