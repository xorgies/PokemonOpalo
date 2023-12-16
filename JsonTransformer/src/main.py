import leerPokemon

ruta = "jsonTransformer/txt/"
rutaJson = "jsonTransformer/json/"
ficheroPokemon = "pokemon.txt"
ficheroEncuentros = "encounters.txt"

print("=======================================")
print("Leyendo pokemons en {}{}".format(ruta,ficheroPokemon))
leerPokemon.leerFicheroPokemon(ruta,ficheroPokemon,rutaJson)
print("=======================================")
print("Fin de leer pokemons")
print("=======================================")

#print("=======================================")
#print("Leyendo encuentros en {}/{}".format(ruta,ficheroEncuentros))
#leerEncuentros(ruta,ficheroEncuentros)
#print("=======================================")
#print("Fin de leer encuentros")
#print("=======================================")