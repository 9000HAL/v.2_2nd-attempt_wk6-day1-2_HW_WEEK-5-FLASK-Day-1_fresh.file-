from flask import request, render_template, redirect, url_for, flash
import requests
from app.forms import LoginForm, SignUpForm
from app import app, db
from app.models import User
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, current_user, login_required

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')





#############################################pokemon_name#############################################
@app.route('/pokemon_name', methods=['GET', 'POST'])
def pokemon_name():
    pokemon_data = None
    if request.method == 'POST':
        pokemon_name = request.form.get('pokemon_name').lower() 
        pokemon_data = get_pokemon_data(pokemon_name)
    return render_template('pokemon_name.html', title='Pokemon Page', pokemon_data=pokemon_data)

def get_pokemon_data(pokemon_name):
    base_url = "https://pokeapi.co/api/v2/"
    url = base_url + f"pokemon/{pokemon_name}/"
    response = requests.get(url)
    data = response.json()

    name = data['name']
    stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
    front_shiny_sprite = data['sprites']['front_shiny']
    ability = data['abilities'][0]['ability']['name']
    
    return {'name': name, 'hp': stats['hp'], 'defense': stats['defense'], 'attack': stats['attack'], 'front_shiny_sprite': front_shiny_sprite, 'ability': ability}




###################################



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data.lower()
        password = form.password.data
        queried_user = User.query.filter(User.email == email).first()
        if queried_user and queried_user.check_password(password):
            login_user(queried_user)
            flash(f'Welcome back {queried_user.first_name}!', 'success')
            return redirect(url_for('home'))
        else:
            error = 'INVALID EMAIL OR PASSWORD'
            return render_template('login.html', form=form, error=error)
    else:
        print('not validated')
        return render_template('login.html', form=form)



@app.route('/signup' , methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if request.method == 'POST' and form.validate_on_submit():
        new_user = User()
        new_user.first_name = form.first_name.data
        new_user.last_name = form.last_name.data
        new_user.email = form.email.data.lower()
        new_user.set_password(form.password.data) # Setting the hashed password.
        print("Hashed password:", new_user.password_hash)



        db.session.add(new_user)
        db.session.commit()

        flash(f"Thank you for signing up {new_user.first_name}!", 'success')
        return redirect(url_for('login'))
    else:
        return render_template('signup.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)

#app = Flask(__name__) RE: ABOVE????

##################

###################LOGOUT

@app.route('/logout')
#@login_required
def logout():
        logout_user()
        flash('Successfully logged out', 'warning')
        return redirect(url_for('home'))












































############lecture version below#######################



"""         





from flask import request, render_template, redirect, url_for, flash
import requests
from app.forms import LoginForm, SignUpForm
from app import app, db
from app.models import User
from werkzeug.security import check_password_hash   



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


# DELETED BELOW NO LONGER NEEDED ---- DUPLICATE PROCESS----------------------
#REGISTERED_USERS = {
#    'dylank@thieves.com': {
#        'name': 'Dylan',
#        'password': 'ilovemydog'
#    }
#}






#############################################pokemon_name#############################################



@app.route('/pokemon_name', methods=['GET', 'POST'])
def pokemon_name():
    pokemon_data = None
    if request.method == 'POST':
        pokemon_name = request.form.get('pokemon_name').lower() # for case-insensitive issue
        pokemon_data = get_pokemon_data(pokemon_name)
    return render_template('pokemon_name.html', title='Pokemon Page', pokemon_data=pokemon_data)


# Function to retrieve Pokémon data
def get_pokemon_data(pokemon_name):
    base_url = "https://pokeapi.co/api/v2/"
    url = base_url + f"pokemon/{pokemon_name}/"
    response = requests.get(url)
    data = response.json()

    name = data['name']
    stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
    front_shiny_sprite = data['sprites']['front_shiny']
    ability = data['abilities'][0]['ability']['name']
    
    return {'name': name, 'hp': stats['hp'], 'defense': stats['defense'], 'attack': stats['attack'], 'front_shiny_sprite': front_shiny_sprite, 'ability': ability}

if __name__ == "__main__":
    app.run(debug=True)











    # AUTHENTICATION moved to bottom of page----------------------





  #v.1----------------------

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data.lower()
        password = form.password.data
        queried_user = User.query.filter(User.email == email).first()
        #if queried_user and check_password_hash(queried_user.password_hash, password):
        if queried_user and check_password_hash(queried_user.password, password):
            flash(f'Welcome back {queried_user.first_name}!', 'success')
            return redirect(url_for('home'))
        else:
            error = 'INVALID EMAIL OR PASSWORD'
            return render_template('login.html', form=form, error=error)
    else:
        print('not validated')
        return render_template('login.html', form=form)





v.2 --- still error----------------------do not use this one

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data.lower()
        password = form.password.data
        queried_user = User.query.filter(User.email == email).first()
        if queried_user and check_password_hash(queried_user.password_hash, password):  # Change this line
            flash(f'Welcome back {queried_user.first_name}!', 'success')
            return redirect(url_for('home'))
        else:
            error = 'INVALID EMAIL OR PASSWORD'
            return render_template('login.html', form=form, error=error)
    else:
        print('not validated')
        return render_template('login.html', form=form)






# sign up form #############################################
@app.route('/signup' , methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if request.method == 'POST' and form.validate_on_submit():

        #this data is coming from the form for signup
        user_data = {
            'first_name': form.first_name.data,
            'last_name': form.last_name.data,
            'email': form.email.data.lower(),
            'password': form.password.data
        }

        #create user instance
        new_user = User()

        # set user_data to our USER ATTRIBUTES
        #new_user.from_dict(user_data) -----attempted to use this but it did not work

        #non-clean approach lol THAT WORKS
        new_user.first_name = user_data['first_name']
        new_user.last_name = user_data['last_name']
        new_user.email = user_data['email']
        new_user.password = new_user.hash_password(user_data['password'])

        
        

        # save to the database
        db.session.add(new_user)
        db.session.commit()

        flash(f"Thank you for signing up {user_data['first_name']}!", 'success')
        return redirect(url_for('login'))
    else:
        return render_template('signup.html', form=form)



"""