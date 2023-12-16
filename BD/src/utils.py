import sqlite3
import json

nombreTablaPokemon="Pokemon"
nombreTablaHabilidades="Habilidades"
nombreTablaHabilidadesPokemon="Pokemon_Habilidades"

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
                                    REFERENCES Pokemon(id),
                                CONSTRAINT fk_habilidad
                                    FOREIGN KEY (habilidad_id)
                                    REFERENCES Habilidades(id)
                            )""")
        print("Se creo la tabla Habilidades_Pokemon")                        
    except sqlite3.OperationalError:
        print("La tabla Habilidades_Pokemon ya existe")


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