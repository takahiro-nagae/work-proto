from flask import render_template

ROOT = 'error/'

def build_error_message(error):
    return error.description if hasattr(error, 'description') else 'Bad Request'


def setup_error_handlers(app):
    @app.errorhandler(400)
    def bad_request(error):
        return render_template(ROOT + '400.html', error_message=build_error_message(error)), 400

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template(ROOT + '404.html'), 404
