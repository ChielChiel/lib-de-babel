# app.py
from flask import Flask, render_template, request, jsonify
from libra.library_de_babel import Library_de_babel

app = Flask(__name__)
bib = Library_de_babel(page_size=80 * 40)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/browse')
def browse():
    report = bib.creat_page(0)
    return render_template("page.html", page_number=0, output=report)

@app.route('/search')
def search_page():
    return render_template("search.html")

@app.route('/page')
def page():
    return render_template("page.html", page_number=313, output='a' * 3200)

@app.route('/random')
def random_page():
    return render_template("page.html", page_number=212, output="d" * 3200)


@app.route('/librarian/lookup', methods=['POST'])
def librarian_lookup():
    if request.method == 'POST':
        text = ""
        try:
            text = request.get_json().get('input_search')
        except:
            print("didnt go well:", text)
        
        number = bib.search(search_string=text)
        # print("requested", number)
        #will be using base-29 for position of pages
        # fetched_result = bib.base29_to_number(bases)
        # report = bib.creat_page(numb=number)
        return {"report": str(number)}
    else:
        return {"result": "niet huts"}

@app.route('/librarian', methods=['POST'])
def librarian():
    if request.method == 'POST':
        # print("zeer zeker post")
        # # print(request.headers)
        # print(request.get_json())
        # print(request.get_json().get("input_number"))
        
        # print("end shit")
        text = request.get_json().get('input_number')
        action = request.get_json().get('action')
        # print("length of input:", len(text))
        try:
            number = int(text,10)
        except:
            print("didnt go well:", text)
        
        number += int(action)
        # print("requested", number)
        #will be using base-29 for position of pages
        # fetched_result = bib.base29_to_number(bases)
        report = bib.creat_page(numb=number)
        return {"number": str(number), "report": report}
    else:
        return {"result": "niet huts"}
