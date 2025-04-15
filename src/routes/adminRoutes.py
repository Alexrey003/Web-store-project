from flask import Blueprint, render_template
from flask_login import login_required, current_user

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin-dashboard')
@login_required
def index():
    if current_user.rol != 'admin':
        return "Acceso denegado", 403
    else:
        return render_template('./admin/index_admin.html')

@admin_bp.route('/admin-dashboard/manage-products')
@login_required
def manage_products():
    if current_user.rol != 'admin':
        return "Acceso denegado", 403
    else:
        return render_template('./admin/manage_products.html')

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