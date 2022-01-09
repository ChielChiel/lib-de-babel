# app.py
from flask import Flask, render_template, request, jsonify
from libra.library_de_babel import Library_de_babel

app = Flask(__name__)
bib = Library_de_babel(page_size=80 * 40)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/browse')
@app.route('/browse/<page_nr>')
def browse(page_nr = '0'):
    page_numb = bib.base29_to_number(base_29=page_nr)
    report = bib.create_page(page_number=page_numb)
    return render_template("page.html", page_number=page_numb, output=report)


@app.route('/search')
def search_page():
    return render_template("search.html")

@app.route('/page')
def page():
    return render_template("page.html", page_number=313, output='a' * 3200)

@app.route('/random')
def random_page():
    rnd = bib.random_base(base_number=29,length=3200)
    page_numb = bib.base29_to_number(base_29=rnd)
    report = bib.create_page(page_number=page_numb)
    return render_template("page.html", page_number=page_numb, output=report)



@app.route('/librarian/lookup', methods=['POST'])
def librarian_lookup():
    if request.method == 'POST':
        text = ""
        try:
            text = request.get_json().get('input_search')
        except:
            print("didnt go well:", text)
        
        number = bib.search(search_string=text)

        return {"report": str(bib.number_to_base29(number=number))}
    else:
        return {"result": "niet huts"}

@app.route('/librarian', methods=['POST'])
def librarian():
    if request.method == 'POST':    
        text = request.get_json().get('input_number')
        action = request.get_json().get('action')

        try:
            number = int(text,10)
        except:
            print("didnt go well:", text)
        
        number += int(action)
        
        report = bib.create_page(page_number=number)
        return {"number": str(number), "report": report}
    else:
        return {"result": "niet huts"}
