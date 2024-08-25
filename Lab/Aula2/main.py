from database import Database
from pokedex import Pokedex
from helper.writeAJson import writeAJson

# Criar uma instância da classe Database
db = Database(database="pokedex", collection="pokemons")

# Criar uma instância da classe Pokedex utilizando a instância de Database
pokedex = Pokedex(db)

tipo = ["Ground"]
 # Utiliza a função `tipopokemon` da classe Pokedex
pokedex.tipopokemon(tipo)
pokedex.eletrico()
pokedex.piscogelo()
pokedex.getPokemonByName("Electabuzz")
pokedex.pokemonsfogo()