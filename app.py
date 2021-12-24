# app.py
from flask import Flask, render_template, request, jsonify
from libra.library_de_babel import Library_de_babel

app = Flask(__name__)


@app.route("/")
@app.route("/<number>")
def index(number = 20):
    bib = Library_de_babel(page_size=80 * 40)
    number = int(number)
    report = bib.creat_page(number)
    return render_template('page.html', name="La bibliotheca de Babel", output=report)
    # return "<center><h1>La Bibliotheca de Babel</h1></center>"


# @app.route("/librarian", methods=['GET'])
# def librarian():
#     return "huts"