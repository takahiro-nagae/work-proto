from flask import Blueprint, request, render_template

app = Blueprint('func', __name__)


@app.route('/analyze_number', methods=['POST'])
def analyze_number():
    num = int(request.form.get('num'))

    data = {
        'number': num,
        'is_even': num % 2 == 0
    }

    return render_template('analyze_number.html', **data)
