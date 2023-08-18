from flask import request, render_template
import requests
#from app.blueprints.main import app  #GHCP -----check DK version????
from . import main
#from flask import Blueprint      #---- GHCP commented out????use???
from flask_login import login_required


@main.route('/')
@main.route('/home') ###########gabe fix???
def home():
    return render_template('home.html')



#############################################pokemon_name#############################################
@main.route('/pokemon', methods=['GET', 'POST'])
#@login_required           #------dk version
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



