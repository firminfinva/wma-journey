import requests
import json 
from flask import Flask, render_template, request
from utils import fetchData

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def search():
    search = request.args.get('search', '')
    data =  fetchData(search)
    return render_template("results.html", data=data)


if __name__ == "__main__":
    app.run()