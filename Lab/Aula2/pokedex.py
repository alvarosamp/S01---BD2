from helper import writeAJson
from database import Database
from helper.writeAJson import writeAJson
class Pokedex:
    def __init__(self, database):
        self.database = database

    def tipopokemon(self, tipos: list):
        db = Database(database="pokedex", collection="pokemons")
        tipos = ["Grass", "Poison"]
        pokemons = list(db.collection.find({"type": {"$in": tipos}, "next_evolution": {"$exists": True}}))
        writeAJson(pokemons, "Pokemons do tipo grama ou veneno que tem evolução")

    def piscogelo(self):
        db = Database(database="pokedex", collection="pokemons")
        fraquezas = ["Psychic", "Ice"]
        pokemons = list(db.collection.find({"weakness": {"$all": fraquezas}}))
        writeAJson(pokemons, "Pokemons fracos contra psico e gelo")

    def getPokemonByName(self, name: str):
        db = Database(database="pokedex", collection="pokemons")
        name = list(db.collection.find({"name": name}))
        writeAJson(name, "Nome do pokemon")

    def pokemonsfogo(self):
        db = Database(database="pokedex", collection="pokemons")
        water = list(db.collection.find({"types": "Water"}))
        writeAJson(water, "Pokemons do tipo agua")

    def eletrico(self):
        db = Database(database="pokedex", collection="pokemons")
        eletricos = list(db.collection.find({"types": "Electric", "weakness": "Fire"}))
        writeAJson(eletricos, "Os pokemons eletricos fracos a fogo são")
