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
    
#AGREGUE ESTAS NUEVAS FUNCIONES
    @classmethod
    def delete_user(self, db, user_id):
        try:
            cursor = db.cursor()
            sql = "DELETE FROM users WHERE user_id = %s"
            cursor.execute(sql, (user_id,))
            db.commit()
            cursor.close()
            print("User deleted succesfuly")
            return True
        except Exception as e:
            print("fError deleting user: {e}")
            return False
    
    @classmethod
    def update_user(self, db, user_id, name, lastname, address, phone, email, username, password):
        try:
            cursor = db.cursor()
            sql = """UPDATE users SET
                    name = %s,
                    lastname = %s,
                    address = %S,
                    phone = %s,
                    email = %s,
                    password = %s
                    WHERE user_id = %s"""
            cursor.execute(sql, (name, lastname, address, phone, email, check_password_hash(password), user_id))
            db.commit()
            cursor.close()
            print("User updated succesfuly")
            return True
        except Exception as e:
            print(f"Error updating user: {e}")
            return False
    
    @classmethod
    def get_all_users(self, db):
        try:
            cursor = db.cursor(dictionary=True)
            sql = "SELECT * FROM users"
            cursor.execute(sql)
            users = cursor.fetchall()
            cursor.close()
            return users
        except Exception as e:
            print(f"Error getting all the users: {e}")
            return None
