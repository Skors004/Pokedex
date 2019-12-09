from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "Pokemon Database"

@app.route("/get")
def get():
    pokemon = request.args.get('name')
    print(pokemon)
    url = "http://pokeapi.co/api/v2/pokemon/"
    apiURL = url + pokemon
    response = requests.get(apiURL)
    data = response.json()
    moves = data["moves"]
    moves = moves[0]
    moves = moves["move"]
    moves = moves["name"]
    species = data["species"]
    speciesURL = species["url"]
    speciesURL = requests.get(speciesURL)
    speciesURL = speciesURL.json()
    speciesURL = speciesURL["flavor_text_entries"]
    species = species["name"]
    picture = data["sprites"]
    picture = picture["front_default"]
    gameNames = ["moon", "alpha-sapphire","blue","gold", "silver", 
                "crystal", "firered", "emerald", "heartgold", "x", "sun"]
    description = ""
    for i in speciesURL:
        if(i["language"]["name"] == "en"):
            if(i["version"]["name"] in gameNames):
                description = description + " " + i["flavor_text"].encode("ascii", "ignore").decode("ascii")
    return render_template('home.html', picture = picture, moves = moves, species = species, description = description)
    
if __name__=="__main__":
    app.run(debug=True)
