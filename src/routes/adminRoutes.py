from flask import Blueprint, render_template
from flask_login import login_required, current_user

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin')
@login_required
def index():
    if current_user.rol != 'admin':
        return "Acceso denegado", 403
    else:
        return render_template('./admin/index_admin.html')