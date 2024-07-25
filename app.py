from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/even_odd', methods=['POST'])
def even_odd():
    num = int(request.form.get('num'))

    data = {
        'number': num,
        'is_even': num % 2 == 0
    }

    return render_template('even_odd.html', **data)


if __name__ == '__main__':
    app.run(debug=True)
