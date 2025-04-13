from werkzeug.security import check_password_hash

class ModelUser():
    @classmethod
    def register_user(self, db, name, lastname, address, phone, email, username, password, rol):
        try:
            cursor = db.cursor()
            sql = "INSERT INTO users (name, lastname, address, phone, email, username, password, rol) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (name, lastname, address, phone, email, username, password, rol)
            cursor.execute(sql, values)
            db.commit()
            cursor.close()
            print("User registered successfully")
            return True
        except Exception as e:
            print(f"Error registering user: {e}")
            return False
    
    @classmethod
    def register_admin(self, db, name, lastname, address, phone, email, username, password, rol):
        try:
            cursor = db.cursor()
            sql = "INSERT INTO users (name, lastname, address, phone, email, username, password, rol) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (name, lastname, address, phone, email, username, password, rol)
            cursor.execute(sql, values)
            db.commit()
            cursor.close()
            print("Admin registered successfully")
            return True
        except Exception as e:
            print(f"Error registering admin: {e}")
            return False
    
    @classmethod
    def login_user(cls, db, username, password):
        try:
            cursor = db.cursor(dictionary=True)
            sql = "SELECT * FROM users WHERE username = %s"
            cursor.execute(sql, (username,))
            user = cursor.fetchone()
            cursor.close()
            if user and check_password_hash(user['password'], password):
                return user
            return None
        except Exception as e:
            print(f"Error logging in user: {e}")
            return None
