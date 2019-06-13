from flask import Flask, render_template, abort, url_for, Blueprint
from werkzeug.utils import redirect

from main.route import main
from fruits.route import fruits
from vegetables.route import vegetables

app = Flask(__name__)

app.register_blueprint(main)
app.register_blueprint(fruits)
app.register_blueprint(vegetables)


if __name__ == '__main__':
    app.run(debug=True)
