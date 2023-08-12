from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String) # Save hashed password.
    created_on = db.Column(db.DateTime, default=datetime.utcnow())

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
















































############lecture version below#######################

"""   
from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String)  
    created_on = db.Column(db.DateTime, default=datetime.utcnow())


    # hashes our password when a user signs up
    def hash_password(new_user, signup_password):        
        return generate_password_hash(signup_password)





##############
    # this method will assign our columns with their respective values ---- WORK ??? --NO DO NOT USE SELF
def from_dict(self, user_data): 
    self.first_name = user_data['first_name']
    self.last_name = user_data['last_name']
    self.email = user_data['email']
    self.password = self.hash_password(user_data['password'])
    --- WORK ??? --NO DO NOT USE SELF
##############

# DUPLICATE MODEL TO FIX ERROR ------WORK ?????????? ---YES!!!!!!
def from_dict(new_user, user_data): 
    new_user.first_name = user_data['first_name']
    new_user.last_name = user_data['last_name']
    new_user.email = user_data['email']
    new_user.password = new_user.hash_password(user_data['password'])


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



    """