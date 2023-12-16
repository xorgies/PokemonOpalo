import sqlite3
import utils

rutaBD="WEB/DB/database.sqlite"

conexion=sqlite3.connect(rutaBD)

utils.crearTablas(conexion)
utils.rellenarPokemons(conexion)
conexion.close()