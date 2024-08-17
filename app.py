from flask import Flask, render_template, request

from analyze_number import analyze_number


def create_app():
    app = Flask(__name__)
    app.register_blueprint(analyze_number.app)

    @app.route('/')
    def home():
        return render_template('home.html')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
