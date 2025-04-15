class ModelHardware():
# This class is used to manage the HARDWARE in the database.
    @classmethod
    def get_all_hardware(self, db):
        try:
            cursor = db.cursor(dictionary=True)
            sql = "SELECT * FROM hardware"
            cursor.execute(sql)
            hardware = cursor.fetchall()
            cursor.close()
            return hardware
        except Exception as e:
            print(f"Error getting all hardware: {e}")
            return None
        
    @classmethod
    def add_hardware(self, db, product_name, specs, category, brand, price, stock, img_url):
        try:
            cursor = db.cursor()
            sql = "INSERT INTO hardware (product_name, specs, category, brand, price, stock, img_url) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (product_name, specs, category, brand, price, stock, img_url)
            cursor.execute(sql, values)
            db.commit()
            cursor.close()
            print("Hardware added successfully")
            return True
        except Exception as e:
            print(f"Error adding hardware: {e}")
            return False
        
    @classmethod
    def delete_hardware(self, db, product_id):
        try:
            cursor = db.cursor()
            sql = "DELETE FROM hardware WHERE id = %s"
            cursor.execute(sql, (product_id,))
            db.commit()
            cursor.close()
            print("Hardware deleted successfully")
            return True
        except Exception as e:
            print(f"Error deleting hardware: {e}")
            return False
    
    @classmethod
    def update_hardware(self, db, product_id, product_name, specs, category, brand, price, stock, img_url):
        try:
            cursor = db.cursor()
            sql = "UPDATE hardware SET product_name = %s, specs = %s, category = %s, brand = %s, price = %s, stock = %s, img_url = %s WHERE id = %s"
            values = (product_name, specs, category, brand, price, stock, img_url, product_id)
            cursor.execute(sql, values)
            db.commit()
            cursor.close()
            print("Hardware updated successfully")
            return True
        except Exception as e:
            print(f"Error updating hardware: {e}")
            return False
class ModelVideogame():
# This class is used to manage the VIDEOGAMES in the database.
    @classmethod
    def get_all_videogame(self, db):
        try:
            cursor = db.cursor(dictionary=True)
            sql = "SELECT * FROM videogames"
            cursor.execute(sql)
            videogames = cursor.fetchall()
            cursor.close()
            return videogames
        except Exception as e:
            print(f"Error getting all videogames: {e}")
            return None
    
    
    @classmethod
    def add_videogame(self, db, game_name, game_description, genre, platforms, price, stock, img_url, release_date, developer):
        try:
            cursor = db.cursor()
            sql = "INSERT INTO videogames (game_name, game_description, genre, brand, platforms, stock, img_url, release_date, developer) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (game_name, game_description, genre, platforms, price, stock, img_url, release_date, developer)
            cursor.execute(sql, values)
            db.commit()
            cursor.close()
            print("Videogame added successfully")
            return True
        except Exception as e:
            print(f"Error adding videogame: {e}")
            return False
    
    
    @classmethod
    def update_videogame(self, db, game_id, game_name, game_description, genre, platforms, price, stock, img_url, release_date, developer):
        try:
            cursor = db.cursor()
            sql = "UPDATE videogames SET game_name = %s, game_description = %s, genre = %s, platforms = %s, price = %s, stock = %s, img_url = %s, release_date = %s, developer = %s WHERE game_id = %s"
            values = (game_name, game_description, genre, platforms, price, stock, img_url,release_date, developer, game_id)
            cursor.execute(sql, values)
            db.commit()
            cursor.close()
            print("Videogame updated successfully")
            return True
        except Exception as e:
            print(f"Error updating videogame: {e}")
            return False
    
    
    @classmethod
    def delete_videogame(self, db, game_id):
        try:
            cursor = db.cursor()
            sql = "DELETE FROM videogames WHERE game_id = %s"
            cursor.execute(sql, (game_id,))
            db.commit()
            cursor.close()
            print("Videogame deleted successfully")
            return True
        except Exception as e:
            print(f"Error deleting videogame: {e}")
            return False