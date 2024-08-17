import json
import os

from flask import Blueprint, render_template

items_bp = Blueprint('items', __name__, template_folder='templates')


@items_bp.route('/items')
def items():
    with open(os.getcwd() + '/items/stocks.json', 'r', encoding='utf-8') as file:
        products = json.load(file)
    return render_template('items.html', products=products)
