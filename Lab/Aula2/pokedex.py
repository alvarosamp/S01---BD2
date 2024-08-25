# Remova ou comente a linha de importação de db
from helper import writeAJson

class Pokedex:
    def __init__(self, database):
        self.database = database


    def tipopokemon(self, tipos: list):
        from main import db  # Importe db dentro do método
        tipos = ["Grass", "Poison"]
        pokemons = db.collection.find({"type": {"$in": tipos}, "next_evolution": {"$exists": True}})
        writeAJson(pokemons, "Pokemons do tipo grama ou veneno que tem evolução")

    # Continue com as outras funções e aplique a mesma modificação
    def piscogelo(self):
        from main import db  # Importe db dentro do método
        fraquezas = ["Psychic", "Ice"]
        pokemons = db.collection.find({"weakness": {"$all": fraquezas}})
        writeAJson(pokemons, "Pokemons fracos contra psico e gelo")

    def getPokemonByName(self, name: str):
        from main import db  # Importe db dentro do método
        name = db.collection.find({"name": name})
        writeAJson(name, "Nome do pokemon")

    def pokemonsfogo(self):
        from main import db  # Importe db dentro do método
        water = db.collection.find({"types": "Water"})
        writeAJson(water, "Pokemons do tipo agua")

    def eletrico(self):
        from main import db  # Importe db dentro do método
        eletricos = db.collection.find({"types": "Eletric", "weakness": "Fire"})
        writeAJson(eletricos, "Os pokemons eletricos fracos a fogo são")
