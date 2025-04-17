from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from models.modelProducts import ModelHardware, ModelVideogame
from database.db_mariadb import db_connect

db = db_connect()
admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin-dashboard')
@login_required
def index():
    if current_user.rol != 'admin':
        return "Acceso denegado", 403
    else:
        return render_template('./admin/index_admin.html')


# ========================== MANAGEMENT PRODUCTS ==========================
# FOR THE MANAGEMENT PRODUCTS PANEL
@admin_bp.route('/admin-dashboard/manage-products', methods=['GET', 'POST'])
@login_required
def manage_products():
    section = request.args.get('section', 'hardware')
    search = request.args.get('search', '')
    
    if section == 'hardware':
        products = ModelHardware.get_all_hardware(db)
        if search:
            products = [p for p in products if search in p['product_name'].lower()]
        for p in products:
            p['id'] = p.get('hardware_id')
    elif section == 'videogames':
        products = ModelVideogame.get_all_videogames(db)
        if search:
            products = [p for p in products if search in p['game_name'].lower()]
        for p in products:
            p['id'] = p.get('game_id')
        
    return render_template('./admin/manage_products.html', products=products, section=section, search=search)

@admin_bp.route('/admin-dashboard/manage-products/add-product', methods=['GET', 'POST'])
@login_required
def add_product():
    data = request.form
    product_type = data.get('product_type')
    
    if product_type == "hardware":
        ModelHardware.add_hardware(
            db,
            data['product_name'],
            data['specs'],
            data['category'],
            data['brand'],
            float(data['price']),
            int(data['stock']),
            data['img_url']
        )
    else:
        ModelVideogame.add_videogame(
            db,
            data['game_name'],
            data['game_description'],
            data['genre'],
            data['platforms'],
            float(data['price']),
            int(data['stock']),
            data['img_url'],
            data['release_date'],
            data['developer']
        )
    return redirect(url_for('admin.manage_products', section=product_type))


@admin_bp.route('/admin-dashboard/manage-products/delete-product/<section>/<int:product_id>', methods=['POST'])
@login_required
def delete_product(section, product_id):
    product_type = request.form.get('product_type')
    
    if product_type == "hardware":
        ModelHardware.delete_hardware(db, product_id)
    elif product_type == "videogames":
        ModelVideogame.delete_videogame(db, product_id)
    
    return redirect(url_for('admin.manage_products', section=product_type))

# ========================== MANAGEMENT USERS ==========================
# FOR THE MANAGEMENT USERS PANEL
@admin_bp.route('/admin-dashboard/manage-users')
@login_required
def manage_users():
    if current_user.rol != 'admin':
        return "Acceso denegado", 403
    else:
        return render_template('./admin/manage_users.html')

@admin_bp.route('/admin-dashboard/see-orders')
@login_required
def see_orders():
    if current_user.rol != 'admin':
        return "Acceso denegado", 403
    else:
        return render_template('./admin/orders.html')

@admin_bp.route('/admin-dashboard/send-email')
@login_required
def send_email():
    if current_user.rol != 'admin':
        return "Acceso denegado", 403
    else:
        return render_template('./admin/email.html')