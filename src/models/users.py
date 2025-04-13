from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, user_id, username, rol):
        self.id = user_id
        self.username = username
        self.rol = rol
    
    @staticmethod
    def get(user_dict):
        return User(user_dict['user_id'], user_dict['username'], user_dict['rol'])


