from flask import Blueprint, render_template, redirect, url_for, abort

main = Blueprint('main', __name__)


@main.route('/')
def main_page():
    return render_template('main.html')


@main.route("/meat")
def test_redirect():
    return redirect(url_for("main_page"))


@main.route("/animal")
def test_abort():
    abort(501, "We are vegans, we have not animals")


@main.errorhandler(501)
def error_505handler(error):
    return render_template("error_501.html")
