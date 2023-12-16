import sqlite3
import utils
import os

rutaBD="WEB/DB/database.sqlite"

try:
    os.remove(rutaBD)
except OSError:
    pass

conexion=sqlite3.connect(rutaBD)

utils.crearTablas(conexion)
utils.rellenarPokemons(conexion)
conexion.close()