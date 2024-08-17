from flask import Flask, render_template, request

from analyze_number import routes as analyze_number
from items import routes as items
from template_filter import resource_filter


def create_app():
    app = Flask(__name__)
    app.register_blueprint(analyze_number.analyze_number_bp)
    app.register_blueprint(items.items_bp)

    app.template_filter('bool_to_symbol')(resource_filter.bool_to_symbol)

    @app.route('/')
    def home():
        return render_template('home.html')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
