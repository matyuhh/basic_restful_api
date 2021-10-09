from werkzeug.security import safe_str_cmp
from user import User

def authenticate(username, password):
    user = User.find_by_username(username)
    if user and user.password == password: #used safe_str_cmp for more security encoding
        return user

def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)