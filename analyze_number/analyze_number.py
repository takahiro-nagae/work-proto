from flask import Blueprint, request, render_template

app = Blueprint('func', __name__)


def is_even(num):
    return num % 2 == 0


def is_prime(num):
    if num <= 1:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for i in range(3, num + 1, 2):
        if num % i == 0:
            return i == num

    return True


@app.route('/analyze_number', methods=['POST'])
def analyze_number():
    num = int(request.form.get('num'))

    data = {
        'number': num,
        'is_even': is_even(num),
        'is_prime': is_prime(num)
    }

    return render_template('analyze_number.html', **data)
