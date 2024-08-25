import hashlib
from database import get_user, add_user

def check_admin(username, password):
    user = get_user(username)
    if user:
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        return user[2] == password_hash and user[3] == 'admin'
    return False

def add_new_user(username, password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    add_user(username, password_hash)

def grant_admin(username):
    user = get_user(username)
    if user:
        add_user(username, user[2], 'admin')
        return True
    return False

