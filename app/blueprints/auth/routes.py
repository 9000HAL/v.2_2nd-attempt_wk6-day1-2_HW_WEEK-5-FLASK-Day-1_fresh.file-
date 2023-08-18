from flask import request, render_template, redirect, url_for, flash
import requests
from app.forms import LoginForm, SignUpForm
from app import app, db
from app.models import User
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, current_user, login_required












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

"""
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


"""
###########swap out GS version BELOW for DK version###########






###################LOGOUT

@app.route('/logout')
#@login_required
def logout():
        logout_user()
        flash('Successfully logged out', 'warning')
        return redirect(url_for('home'))



