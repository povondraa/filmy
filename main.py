from flask import Flask, render_template, request
from data import filmy

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, World!"


@app.route('/filmy')
def get_filmy():
    hledat = request.args.get('hledat', '')
    filtr_filmy = []
    for film in filmy.values():
        if hledat in film['nazev']:
            filtr_filmy.append(film)
    return render_template('filmy.html', filmy=filtr_filmy)


if __name__ == '__main__':
    app.run(debug=True)
