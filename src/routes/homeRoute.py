from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    return render_template('./home/index.html')

@home_bp.route('/products')
def products():
    # return render_template('./home/products.html')
    pass

@home_bp.route('/shopping-cart')
def shopping_cart():
    # return render_template('./home/shopping-cart.html')
    pass