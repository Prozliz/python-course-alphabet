from flask import Blueprint, render_template, request

fruits = Blueprint('fruits', __name__)

fruit_list = ['Apricot', 'Pineapple', 'Banana', 'Grape', 'Grapefruit']


@fruits.route('/fruits')
def fruits_main():
    return render_template('fruits.html', title='Fruits', fruits_list=fruit_list)


@fruits.route('/fruits/<string:value>', methods=['GET', 'POST', 'DELETE'])
def test_methods(value=None):
    if request.method == 'POST':
        do_post(value)
        return "Successfully added a new value"
    if request.method == 'DELETE':
        do_delete(value)
        return "Successfully deleted the value"
    else:
        return do_get()


def do_post(value):
    return fruit_list.append(value)


def do_get():
    return render_template('fruits.html', values=fruit_list)


def do_delete(value):
    for i, elem in enumerate(fruit_list):
        if elem == value:
            fruit_list.pop(i)
