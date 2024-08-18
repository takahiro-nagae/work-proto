from flask import Blueprint, request, render_template, jsonify, abort

from analyze_number.logic import is_even, is_prime, validate

analyze_number_bp = Blueprint('func', __name__, template_folder='templates')


@analyze_number_bp.route('/analyze_number', methods=['POST'])
def analyze_number():
    num_str = request.form.get('num')
    validate(num_str)

    num = int(num_str)

    data = {
        'number': num,
        'is_even': is_even(num),
        'is_prime': is_prime(num)
    }

    return render_template('analyze_number.html', **data)
