import sqlite3
import utils
import os

rutaBD="WEB/DB/database.sqlite3"


conexion=sqlite3.connect(rutaBD)

utils.crearTablas(conexion)
utils.rellenarPokemons(conexion)
conexion.close()