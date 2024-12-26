import leerPokemon
import leerEncuentros
import leerHabilidades
import leerMovimientos

rutaTxt = "jsonTransformer/txt/"
rutaJson = "jsonTransformer/json/"
rutaJuego = "hispalis/"
ficheroPokemon = rutaJuego+"pokemon.txt"
ficheroEncuentros = rutaJuego+"encounters.txt"
ficheroHabilidades = rutaJuego+"abilities.txt"
ficheroMovimientos = rutaJuego+"moves.txt"


print("=======================================")
print("Leyendo habilidades en {}{}".format(rutaTxt,ficheroHabilidades))
leerHabilidades.leerFicheroHabilidades(rutaTxt,ficheroHabilidades,rutaJson)
print("=======================================")
print("Fin de leer habilidades")
print("=======================================")


print("=======================================")
print("Leyendo movimientos en {}{}".format(rutaTxt,ficheroMovimientos))
leerMovimientos.leerFicheroMovimientos(rutaTxt,ficheroMovimientos,rutaJson)
print("=======================================")
print("Fin de leer movimientos")
print("=======================================")


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
