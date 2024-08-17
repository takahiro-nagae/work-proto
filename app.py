from flask import Flask, render_template, request

from analyze_number.routes import analyze_number_bp
from items.routes import items_bp
from template_filter.resource_filter import bool_to_symbol


def create_app():
    app = Flask(__name__)
    app.register_blueprint(analyze_number_bp)
    app.register_blueprint(items_bp)

    app.template_filter('bool_to_symbol')(bool_to_symbol)

    @app.route('/')
    def home():
        return render_template('home.html')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
