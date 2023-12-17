import leerPokemon
import leerEncuentros

rutaTxt = "jsonTransformer/txt/"
rutaJson = "jsonTransformer/json/"
ficheroPokemon = "pokemon.txt"
ficheroEncuentros = "encounters.txt"

print("=======================================")
print("Leyendo pokemons en {}{}".format(rutaTxt,ficheroPokemon))
leerPokemon.leerFicheroPokemon(rutaTxt,ficheroPokemon,rutaJson)
print("=======================================")
print("Fin de leer pokemons")
print("=======================================")

print("=======================================")
print("Leyendo encuentros en {}{}".format(rutaTxt,ficheroEncuentros))
leerEncuentros.leerFicheroEncuentros(rutaTxt,ficheroEncuentros,rutaJson)
print("=======================================")
print("Fin de leer encuentros")
print("=======================================")