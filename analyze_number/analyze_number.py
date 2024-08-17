from flask import Blueprint, request, render_template

app = Blueprint('func', __name__)


def is_even(num):
    return num % 2 == 0


@app.route('/analyze_number', methods=['POST'])
def analyze_number():
    num = int(request.form.get('num'))

    data = {
        'number': num,
        'is_even':  is_even(num)
    }

    return render_template('analyze_number.html', **data)
