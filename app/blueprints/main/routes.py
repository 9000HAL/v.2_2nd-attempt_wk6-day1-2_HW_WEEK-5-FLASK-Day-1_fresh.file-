from flask import request, render_template
import requests
#from app.blueprints.main import app  #GHCP
from . import main
from app import login_required


@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html')





#############################################pokemon_name#############################################
@main.route('/pokemon_name', methods=['GET', 'POST'])
def pokemon_name():
    pokemon_data = None
    if request.method == 'POST':
        pokemon_name = request.form.get('pokemon_name').lower() 
        pokemon_data = get_pokemon_data(pokemon_name)
    return render_template('pokemon.html', title='Pokemon Page', pokemon_data=pokemon_data)

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





#----------comment out the AUTH functions below----------------------
"""     


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data.lower()
        password = form.password.data
        queried_user = User.query.filter(User.email == email).first()
        if queried_user and queried_user.check_password(password):
        #if queried_user and check_password_hash(queried_user.password_hash, password):           #-----DK version------
            login_user(queried_user)
            flash(f'Welcome back {queried_user.first_name}!', 'success')
            return redirect(url_for('home'))
        else:
            error = 'INVALID EMAIL OR PASSWORD'
            return render_template('login.html', form=form, error=error)
    else:
        print('not validated')
        return render_template('login.html', form=form) 



######################################################

##########DK signup version##########

app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if request.method == 'POST' and form.validate_on_submit():

        #data from signup form
        user_data = {
            'first_name': form.first_name.data,
            'last_name': form.last_name.data,
            'email': form.email.data.lower(),
            'password': form.password.data
        
        }

        #create new user instance
        new_user = User()

        #set user_data to our user attributes
        new_user.from_dict(user_data)

        #save to db
        db.session.add(new_user)
        db.session.commit()


        flash(f'Thank you for signing up {user_data["first_name"]}!', 'success')
        return redirect(url_for('login'))
    else:
        return render_template('signup.html', form=form)


######################################################





###########swap out GS version BELOW for DK version###########


@app.route('/signup', methods=['GET', 'POST'])
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

###########swap out GS version for DK version###########







###################LOGOUT

@app.route('/logout')
#@login_required
def logout():
        logout_user()
        flash('Successfully logged out', 'warning')
        return redirect(url_for('home'))



"""