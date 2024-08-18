from flask import Blueprint, render_template

from items.logic import load_json, build_dict_for_list

items_bp = Blueprint('items', __name__, template_folder='templates')

@items_bp.route('/items')
def items():
    products = load_json('products.json')
    stocks = load_json('stocks.json')
    prices = load_json('prices.json')

    stocks_dict = build_dict_for_list(stocks, 'id', 'stock')
    prices_dict = build_dict_for_list(prices, 'id', 'price')

    items = []
    for product in products:
        id = product['id']
        product['stock'] = stocks_dict.get(id)
        product['price'] = prices_dict.get(id)

        items.append(product)

    return render_template('items.html', items=items)
