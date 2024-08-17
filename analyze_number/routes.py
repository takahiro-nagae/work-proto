from flask import Blueprint, request, render_template

from analyze_number.logic import is_even, is_prime

analyze_number_bp = Blueprint('func', __name__, template_folder='templates')


@analyze_number_bp.route('/analyze_number', methods=['POST'])
def analyze_number():
    num = int(request.form.get('num'))

    data = {
        'number': num,
        'is_even': is_even(num),
        'is_prime': is_prime(num)
    }

    return render_template('analyze_number.html', **data)
