import sqlite3
import utils
import os

rutaBD="WEB/DB/database.sqlite3"

try:
    os.remove(rutaBD)
except OSError:
    pass

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
print("==============================")
print("Rellenando tablas Estadisticas")
utils.rellenarEstadisticas(conexion)
print("==============================")
print("Rellenando tablas Tipos")
utils.rellenarTipos(conexion)
print("==============================")
print("Rellenando tablas Movimientos")
utils.rellenarMovimientos(conexion)
print("==============================")
print("Rellenando tablas Evoluciones")
utils.rellenarEvoluciones(conexion)

conexion.close()