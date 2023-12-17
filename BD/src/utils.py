import sqlite3
import json

nombreTablaPokemon="Pokemon"
nombreTablaHabilidades="Habilidades"
nombreTablaHabilidadesPokemon="Pokemon_Habilidades"
nombreTablaEstadisticasPokemon="Pokemon_Estadisticas"
nombreTablaTipos="Tipos"
nombreTablaTiposPokemon="Pokemon_Tipos"
nombreTablaMovimientos="Movientos"
nombreTablaMovimientosPokemon="Pokemon_Movimientos"
nombreTablaEvoluciones="Evoluciones"

def crearTablas(conexion):
    ##########################################
    # tablas principales

    # Pokemon
    try:
        conexion.execute(f"""create table {nombreTablaPokemon} (
                                id integer primary key,
                                name text,
                                genderRate text,
                                growthRate text,
                                rareness integer,
                                happiness integer,
                                compatibility text,
                                stepsToHatch integer,
                                height real,
                                weight real,
                                color text,
                                pokedex text
                            )""")
        print("Se creo la tabla Pokemon")                        
    except sqlite3.OperationalError:
        print("La tabla Pokemon ya existe")  

    # Habilidades                  
    try:
        conexion.execute(f"""create table {nombreTablaHabilidades} (
                                id integer primary key,
                                nombre text
                            )""")
        print("Se creo la tabla Habilidades")                        
    except sqlite3.OperationalError:
        print("La tabla Habilidades ya existe")
    
    # Tipos                  
    try:
        conexion.execute(f"""create table {nombreTablaTipos} (
                                id integer primary key,
                                nombre text
                            )""")
        print("Se creo la tabla Tipos")                        
    except sqlite3.OperationalError:
        print("La tabla Tipos ya existe")

    # Movimientos                  
    try:
        conexion.execute(f"""create table {nombreTablaMovimientos} (
                                id integer primary key,
                                nombre text
                            )""")
        print("Se creo la tabla Movimientos")                        
    except sqlite3.OperationalError:
        print("La tabla Movimientos ya existe")

    ##########################################
    # tablas con relaciones

    # Pokemon_Habilidades
    try:
        conexion.execute(f"""create table {nombreTablaHabilidadesPokemon} (
                                pokemon_id integer,
                                habilidad_id integer,
                                tipo text,
                                CONSTRAINT fk_pokemon
                                    FOREIGN KEY (pokemon_id)
                                    REFERENCES {nombreTablaPokemon}(id),
                                CONSTRAINT fk_habilidad
                                    FOREIGN KEY (habilidad_id)
                                    REFERENCES {nombreTablaHabilidades}(id)
                            )""")
        print("Se creo la tabla Pokemon_Habilidades")                        
    except sqlite3.OperationalError:
        print("La tabla Pokemon_Habilidades ya existe")

    # Pokemon_Estadisticas                  
    try:
        conexion.execute(f"""create table {nombreTablaEstadisticasPokemon} (
                                id integer primary key autoincrement,
                                pokemon_id integer,
                                ps integer,
                                atk integer,
                                def integer,
                                spd integer,
                                atk_sp integer,
                                def_sp integer,
                                CONSTRAINT fk_pokemon
                                    FOREIGN KEY (pokemon_id)
                                    REFERENCES {nombreTablaPokemon}(id)
                            )""")
        print("Se creo la tabla Pokemon_Estadisticas")                        
    except sqlite3.OperationalError:
        print("La tabla Pokemon_Estadisticas ya existe")
    
    # Pokemon_Tipos
    try:
        conexion.execute(f"""create table {nombreTablaTiposPokemon} (
                                pokemon_id integer,
                                tipo_id integer,
                                CONSTRAINT fk_pokemon
                                    FOREIGN KEY (pokemon_id)
                                    REFERENCES {nombreTablaPokemon}(id),
                                CONSTRAINT fk_tipo
                                    FOREIGN KEY (tipo_id)
                                    REFERENCES {nombreTablaTipos}(id)
                            )""")
        print("Se creo la tabla Pokemon_Tipos")                        
    except sqlite3.OperationalError:
        print("La tabla Pokemon_Tipos ya existe")

    # Pokemon_Movimientos
    try:
        conexion.execute(f"""create table {nombreTablaMovimientosPokemon} (
                                pokemon_id integer,
                                movimiento_id integer,
                                nivel_aprender text,
                                CONSTRAINT fk_pokemon
                                    FOREIGN KEY (pokemon_id)
                                    REFERENCES {nombreTablaPokemon}(id),
                                CONSTRAINT fk_movimiento
                                    FOREIGN KEY (movimiento_id)
                                    REFERENCES {nombreTablaMovimientos}(id)
                            )""")
        print("Se creo la tabla Pokemon_Movimientos")                        
    except sqlite3.OperationalError:
        print("La tabla Pokemon_Movimientos ya existe")

    # Evoluciones
    try:
        conexion.execute(f"""create table {nombreTablaEvoluciones} (
                                pokemon_id integer,
                                pokemon_evolucion_id integer,
                                forma text,
                                descripcion text,
                                CONSTRAINT fk_pokemon
                                    FOREIGN KEY (pokemon_id)
                                    REFERENCES {nombreTablaPokemon}(id),
                                CONSTRAINT fk_pokemon_evolucion
                                    FOREIGN KEY (pokemon_evolucion_id)
                                    REFERENCES {nombreTablaPokemon}(id)
                            )""")
        print("Se creo la tabla Evoluciones")                        
    except sqlite3.OperationalError:
        print("La tabla Evoluciones ya existe")

def rellenarPokemons(conexion):
    with open("JsonTransformer/json/pokemon.json") as file:
        data = json.load(file)
        for pokemon in data['pokemons']:
            try:
                conexion.execute("insert into "+nombreTablaPokemon+"(id,name,genderRate,growthRate,rareness,happiness,compatibility,stepsToHatch,height,weight,color,pokedex) values (?,?,?,?,?,?,?,?,?,?,?,?)", (pokemon['id'], pokemon['Name'], pokemon['GenderRate'],pokemon['GrowthRate'],pokemon['Rareness'],pokemon['Happiness'],pokemon['Compatibility'],pokemon['StepsToHatch'],pokemon['Height'],pokemon['Weight'],pokemon['Color'],pokemon['Pokedex']))
                conexion.commit()
            except:
                print("Ya existe la fila")
                

def rellenarHabilidades(conexion):
    with open("JsonTransformer/json/habilidades.json") as file:
        data = json.load(file)
        for (id, nombre) in data.items():
            try:
                conexion.execute("insert into "+nombreTablaHabilidades+"(id,nombre) values (?,?)", (id, nombre))
                conexion.commit()
            except:
                print("Ya existe la fila")

    with open("JsonTransformer/json/habilidades_pokemon.json") as file:
        data = json.load(file)
        for habilidad_pokemon in data['habilidades']:
            try:
                conexion.execute("insert into "+nombreTablaHabilidadesPokemon+"(pokemon_id,habilidad_id,tipo) values (?,?,?)", (habilidad_pokemon['pokemon_id'],habilidad_pokemon['habilidad_id'],habilidad_pokemon['tipo']))
                conexion.commit()
            except:
                print("Ya existe la fila")

def rellenarEstadisticas(conexion):
    with open("JsonTransformer/json/estadisticas_pokemon.json") as file:
        data = json.load(file)
        for estadisticas_pokemon in data['estadisticas']:
            try:
                conexion.execute("insert into "+nombreTablaEstadisticasPokemon+"(pokemon_id,ps,atk,def,spd,atk_sp,def_sp) values (?,?,?,?,?,?,?)", (estadisticas_pokemon['pokemon_id'],estadisticas_pokemon['ps'],estadisticas_pokemon['atk'],estadisticas_pokemon['def'],estadisticas_pokemon['spd'],estadisticas_pokemon['atk_sp'],estadisticas_pokemon['def_sp']))
                conexion.commit()
            except:
                print("Ya existe la fila")

def rellenarTipos(conexion):
    with open("JsonTransformer/json/tipos.json") as file:
        data = json.load(file)
        for (id, nombre) in data.items():
            try:
                conexion.execute("insert into "+nombreTablaTipos+"(id,nombre) values (?,?)", (id, nombre))
                conexion.commit()
            except:
                print("Ya existe la fila")

    with open("JsonTransformer/json/tipos_pokemon.json") as file:
        data = json.load(file)
        for tipo_pokemon in data['tipos']:
            try:
                conexion.execute("insert into "+nombreTablaTiposPokemon+"(pokemon_id,tipo_id) values (?,?)", (tipo_pokemon['pokemon_id'],tipo_pokemon['tipo_id']))
                conexion.commit()
            except:
                print("Ya existe la fila")

def rellenarMovimientos(conexion):
    with open("JsonTransformer/json/movimientos.json") as file:
        data = json.load(file)
        for (id, nombre) in data.items():
            try:
                conexion.execute("insert into "+nombreTablaMovimientos+"(id,nombre) values (?,?)", (id, nombre))
                conexion.commit()
            except:
                print("Ya existe la fila")

    with open("JsonTransformer/json/movimientos_pokemon.json") as file:
        data = json.load(file)
        for movimiento_pokemon in data['movimientos']:
            try:
                conexion.execute("insert into "+nombreTablaMovimientosPokemon+"(pokemon_id,movimiento_id,nivel_aprender) values (?,?,?)", (movimiento_pokemon['pokemon_id'],movimiento_pokemon['movimiento_id'],movimiento_pokemon['nivel_aprender']))
                conexion.commit()
            except:
                print("Ya existe la fila")

def rellenarEvoluciones(conexion):
    with open("JsonTransformer/json/evoluciones_pokemon.json") as file:
        data = json.load(file)
        for evoluciones_pokemon in data['evoluciones']:
            try:
                conexion.execute("insert into "+nombreTablaEvoluciones+"(pokemon_id,pokemon_evolucion_id,forma,descripcion) values (?,?,?,?)", (evoluciones_pokemon['pokemon_id'],evoluciones_pokemon['pokemon_evolucion_id'],evoluciones_pokemon['forma'],evoluciones_pokemon['descripcion']))
                conexion.commit()
            except:
                print("Ya existe la fila")