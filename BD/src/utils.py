import sqlite3
import json

nombreTablaPokemon="Pokemon"
nombreTablaHabilidades="Habilidades"
nombreTablaHabilidadesPokemon="Pokemon_Habilidades"
nombreTablaEstadisticasPokemon="Pokemon_Estadisticas"
nombreTablaTipos="Tipos"
nombreTablaTiposPokemon="Pokemon_Tipos"
nombreTablaMovimientos="Movimientos"
nombreTablaMovimientosPokemon="Pokemon_Movimientos"
nombreTablaEvoluciones="Evoluciones"
nombreTablaLugares="Lugares"
nombreTablaEncuentros="Encuentros"

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
                                pokedex text,
                                eggMoves text
                            )""")
        print("Se creo la tabla Pokemon")                        
    except sqlite3.OperationalError:
        print("La tabla Pokemon ya existe")  

    # Habilidades                  
    try:
        conexion.execute(f"""create table {nombreTablaHabilidades} (
                                id integer primary key,
                                nombre text,
                                nombre_esp text,
                                descripcion text
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
                                nombre text,
                                nombre_esp text,
                                potencia integer,
                                tipo text,
                                clase text,
                                precision integer,
                                pp integer,
                                descripcion text
                            )""")
        print("Se creo la tabla Movimientos")                        
    except sqlite3.OperationalError:
        print("La tabla Movimientos ya existe")
    
    # Movimientos                  
    try:
        conexion.execute(f"""create table {nombreTablaLugares} (
                                id integer primary key,
                                nombre text
                            )""")
        print("Se creo la tabla Lugares")                        
    except sqlite3.OperationalError:
        print("La tabla Lugares ya existe")

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
                                nivel_aprender integer,
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
                                primary key(pokemon_id,pokemon_evolucion_id)
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

    # Encuentros                  
    try:
        conexion.execute(f"""create table {nombreTablaEncuentros} (
                                id integer primary key autoincrement,
                                pokemon_id integer,
                                nombre text,
                                lugar_id integer,
                                nivel_min integer,
                                nivel_max integer,
                                CONSTRAINT fk_lugar
                                    FOREIGN KEY (lugar_id)
                                    REFERENCES {nombreTablaLugares}(id)
                            )""")
        print("Se creo la tabla Encuentros")                        
    except sqlite3.OperationalError:
        print("La tabla Encuentros ya existe")

def rellenarPokemons(conexion):
    with open("JsonTransformer/json/pokemon.json",encoding='utf-8') as file:
        data = json.load(file)
        for pokemon in data['pokemons']:
            try:
                if 'EggMoves' in pokemon.keys():
                    conexion.execute("insert into "+nombreTablaPokemon+"(id,name,genderRate,growthRate,rareness,happiness,compatibility,stepsToHatch,height,weight,color,pokedex,eggMoves) values (?,?,?,?,?,?,?,?,?,?,?,?,?)", (pokemon['id'], pokemon['Name'], pokemon['GenderRate'],pokemon['GrowthRate'],pokemon['Rareness'],pokemon['Happiness'],pokemon['Compatibility'],pokemon['StepsToHatch'],pokemon['Height'],pokemon['Weight'],pokemon['Color'],pokemon['Pokedex'],pokemon['EggMoves']))
                else:
                    conexion.execute("insert into "+nombreTablaPokemon+"(id,name,genderRate,growthRate,rareness,happiness,compatibility,stepsToHatch,height,weight,color,pokedex) values (?,?,?,?,?,?,?,?,?,?,?,?)", (pokemon['id'], pokemon['Name'], pokemon['GenderRate'],pokemon['GrowthRate'],pokemon['Rareness'],pokemon['Happiness'],pokemon['Compatibility'],pokemon['StepsToHatch'],pokemon['Height'],pokemon['Weight'],pokemon['Color'],pokemon['Pokedex']))
                conexion.commit()
            except Exception as error:
                print("Ya existe la fila")
                

def rellenarHabilidades(conexion):
    with open("JsonTransformer/json/habilidades.json",encoding='utf-8') as file:
        data = json.load(file)
        for (id, habilidad) in data.items():
            try:
                conexion.execute("insert into "+nombreTablaHabilidades+"(id,nombre,nombre_esp,descripcion) values (?,?,?,?)", (id, habilidad['nombre'],habilidad['nombre_esp'],habilidad['descripcion']))
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
    with open("JsonTransformer/json/movimientos.json",encoding='utf-8') as file:
        data = json.load(file)
        for (id, movimiento) in data.items():
            try:
                conexion.execute("insert into "+nombreTablaMovimientos+"(id,nombre,nombre_esp,potencia,tipo,clase,precision,pp,descripcion) values (?,?,?,?,?,?,?,?,?)", (id, movimiento['nombre'],movimiento['nombre_esp'],movimiento['potencia'],movimiento['tipo'],movimiento['clase'],movimiento['precision'],movimiento['pp'],movimiento['descripcion']))
                conexion.commit()
            except Exception as error:
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
                print("insert into "+nombreTablaEvoluciones+"(pokemon_id,pokemon_evolucion_id,forma,descripcion) values (?,?,?,?)", (evoluciones_pokemon['pokemon_id'],evoluciones_pokemon['pokemon_evolucion_id'],evoluciones_pokemon['forma'],evoluciones_pokemon['descripcion']))

def rellenarLugares(conexion):
    with open("JsonTransformer/json/lugares.json") as file:
        data = json.load(file)
        for (id, nombre) in data.items():
            try:
                conexion.execute("insert into "+nombreTablaLugares+"(id,nombre) values (?,?)", (id, nombre))
                conexion.commit()
            except:
                print("Ya existe la fila")

def rellenarEncuentros(conexion):
    with open("JsonTransformer/json/encuentros.json",encoding='ISO-8859-1') as file:
        data = json.load(file)
        for encuentro in data['encuentros']:
            try:
                conexion.execute("insert into "+nombreTablaEncuentros+"(pokemon_id,nombre,lugar_id,nivel_min,nivel_max) values (?,?,?,?,?)", (encuentro['pokemon_id'],encuentro['nombre'],encuentro['lugar_id'],encuentro['nivel_min'],encuentro['nivel_max']))
                conexion.commit()
            except:
                print("Ya existe la fila")

def crearVistas(conexion):
    # datos_pokemon_view  
    try:
        conexion.execute(f"""create view datos_pokemon_view AS
                                select p.*, pe.ps,pe.atk,pe.def,pe.spd,pe.atk_sp,pe.def_sp
                                FROM {nombreTablaPokemon} p, {nombreTablaEstadisticasPokemon} pe
                                WHERE p.id=pe.pokemon_id
                            """)
        print("Se creo la vista datos_pokemon_view")                        
    except sqlite3.OperationalError:
        print("La vista datos_pokemon_view ya existe")

    # evoluciones_view  
    try:
        conexion.execute(f"""create view evoluciones_view as
                                select p.id,p.name, e.pokemon_evolucion_id,p2.name as name_evolucion,e.forma,e.descripcion  
                                FROM {nombreTablaPokemon} p, {nombreTablaEvoluciones} e, {nombreTablaPokemon} p2
                                where p.id = e.pokemon_id
                                    and p2.id = e.pokemon_evolucion_id
                            """)
        print("Se creo la vista evoluciones_view")                        
    except sqlite3.OperationalError:
        print("La vista evoluciones_view ya existe")

    # pokemon_tipos_view  
    try:
        conexion.execute(f"""create view pokemon_tipos_view as
                                    select p.id,t.nombre
                                    from {nombreTablaPokemon} p,{nombreTablaTiposPokemon} pt,{nombreTablaTipos} t
                                    where p.id = pt.pokemon_id
                                        and t.id = pt.tipo_id
                            """)
        print("Se creo la vista pokemon_tipos_view")                        
    except sqlite3.OperationalError:
        print("La vista pokemon_tipos_view ya existe")

    # pokemon_movimientos_view  
    try:
        conexion.execute(f"""create view pokemon_movimientos_view as
                                select p.id,m.nombre,pm.nivel_aprender,m.nombre_esp,m.potencia,m.tipo,m.clase,m.precision,m.pp,m.descripcion
                                from {nombreTablaPokemon} p,{nombreTablaMovimientosPokemon} pm,{nombreTablaMovimientos} m
                                where p.id = pm.pokemon_id
                                    and m.id = pm.movimiento_id
                            """)
        print("Se creo la vista pokemon_movimientos_view")                        
    except sqlite3.OperationalError:
        print("La vista pokemon_movimientos_view ya existe")
    
    # pokemon_habilidades_view  
    try:
        conexion.execute(f"""create view pokemon_habilidades_view as
                                select p.id,h.nombre,ph.tipo,h.id as habilidad_id,h.nombre_esp,h.descripcion
                                from {nombreTablaPokemon} p,{nombreTablaHabilidadesPokemon} ph,{nombreTablaHabilidades} h
                                where p.id = ph.pokemon_id
                                    and h.id = ph.habilidad_id
                            """)
        print("Se creo la vista pokemon_habilidades_view")                        
    except sqlite3.OperationalError:
        print("La vista pokemon_habilidades_view ya existe")

    # encuentros_lugares_view  
    try:
        conexion.execute(f"""create view encuentros_lugares_view as
                                select e.id, e.pokemon_id, e.nombre, e.nivel_min, e.nivel_max, l.nombre as nombre_lugar
                                from {nombreTablaEncuentros} e, {nombreTablaLugares} l
                                where e.lugar_id = l.id
                            """)
        print("Se creo la vista encuentros_lugares_view")                        
    except sqlite3.OperationalError:
        print("La vista encuentros_lugares_view ya existe")

