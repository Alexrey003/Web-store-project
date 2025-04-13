#Libraries
from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from flask_login import login_user, logout_user, current_user, LoginManager, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf.csrf import CSRFProtect

#Modules
from models.modelUsers import ModelUser
from database.db_mariadb import db_connect
from models.users import User

#Define the blueprints for login and register routes
auth_bp = Blueprint('auth', __name__)

# Database connection
db = db_connect()

# Login route for normal users and admin
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user_data = ModelUser.login_user(db, username, password)

        if user_data:
            user = User.get(user_data)
            login_user(user)
            if user.rol == 'admin':
                return redirect(url_for('admin.index'))
            else:
                return redirect(url_for('home.index'))
        else:
            print('Invalid username or password')
            return redirect(url_for('auth.login'))
    return render_template('./auth/login.html')

# Register route for normal users
@auth_bp.route('/register/user', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        lastname = request.form.get('lastname')
        address = request.form.get('address')
        phone = request.form.get('phone')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        rol = 'user'
        try:
            user = ModelUser.register_user(db, name, lastname, address, phone, email, username, generate_password_hash(password), rol)
            return redirect(url_for('auth.login'))
        except Exception as e:
            return redirect(url_for('auth.register'))
    return render_template('./auth/register.html')

@auth_bp.route('/register/admin', methods=['GET', 'POST'])
def register_admin():
    if request.method == 'POST':
        name = request.form.get('name')
        lastname = request.form.get('lastname')
        address = request.form.get('address')
        phone = request.form.get('phone')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        rol = 'admin'
        try:
            admin = ModelUser.register_user(db, name, lastname, address, phone, email, username, generate_password_hash(password), rol)
            return redirect(url_for('auth.login'))
        except Exception as e:
            return redirect(url_for('auth.register_admin'))
    return render_template('./auth/register_admin.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('home.index'))