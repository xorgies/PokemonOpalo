import sqlite3
import utils
import os

rutaBD="WEB/DB/database.sqlite3"


conexion=sqlite3.connect(rutaBD)

print("==============================")
print("Creando tablas")
utils.crearTablas(conexion)
print("==============================")
print("Rellenando tabla Pokemon")
utils.rellenarPokemons(conexion)
print("==============================")
print("Rellenando tablas Habilidades")
utils.rellenarHabilidades(conexion)

conexion.close()