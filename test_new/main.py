from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/calc')
def calc():
    n1 = 29
    n2 = 235
    return render_template('calc.html',
                           num1 = n1,
                           num2 = n2)

app.run(debug=True)