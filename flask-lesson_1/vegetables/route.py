from flask import Blueprint, render_template, request

vegetables = Blueprint('vegetables', __name__, )

vegetables_list = ['Tomato', 'Carrot', 'Cabbage', 'Pepper', 'Egglant']


@vegetables.route('/vegetables')
def vegetables_main():
    return render_template('vegetables.html', title='Vegetables', vegetables_list=vegetables_list)


@vegetables.route('/vegetables/<string:value>', methods=['GET', 'POST', 'DELETE'])
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
    return vegetables_list.append(value)


def do_get():
    return render_template('vegetables.html', values=vegetables_list)


def do_delete(value):
    for i, elem in enumerate(vegetables_list):
        if elem == value:
            vegetables_list.pop(i)
