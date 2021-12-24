# app.py
from flask import Flask, render_template, request, jsonify
from libra.library_de_babel import Library_de_babel

app = Flask(__name__)
bib = Library_de_babel(page_size=80 * 40)


@app.route("/")
@app.route("/<number>")
def index(number = 20):
    number = int(number)
    report = bib.creat_page(number)
    return render_template('page.html', name="La bibliotheca de Babel", output=report)
    # return "<center><h1>La Bibliotheca de Babel</h1></center>"

@app.route('/search')
def method_name():
    katshuis = bib.string_to_base(' ' * 40*80)
    # print(katshuis)
    to_see = bib.arynth(katshuis)
    print(f"{to_see=}")
    return f"<p>{to_see}</p><br><br><p>{4.7**4680}</p>"

@app.route('/librarian')
@app.route('/librarian/<bases>')
def librarian(bases = '0'):
    #will be using base-29 for position of pages
    fetched_result = bib.base29_to_number(bases)
    report = bib.creat_page(fetched_result)
    return render_template('page.html', name="La bibliotheca de Babel", output=report)

# @app.route("/librarian", methods=['GET'])
# def librarian():
#     return "huts"