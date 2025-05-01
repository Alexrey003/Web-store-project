from flask import flash

def validate_user_registration(form_data, db):
    required_fields = ['name,', 'lastname', 'address', 'phone', 'email', 'username', 'password']
    for field in required_fields:
        if not form_data.get(field):
            flash(f"El campo {field} es obligatorio", "error")
            return False
        if len(form_data['password']) < 6:
            flash("La contraseña debe tener al menos 6 o más caracteres", "error")
            return False
        
        # cursor = db.cursor()
        # sql = "SELECT username, email FROM users"
        # cursor.execute(sql)
        # users = cursor.fetchall()
        
        return True