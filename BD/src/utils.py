import sqlite3
import json

def crearTablas(conexion):
    try:
        conexion.execute("""create table Pokemon (
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

def rellenarPokemons(conexion):
    with open("JsonTransformer/json/pokemon.json") as file:
        data = json.load(file)
        for pokemon in data['pokemons']:
            conexion.execute("insert into Pokemon(id,name,genderRate,growthRate,rareness,happiness,compatibility,stepsToHatch,height,weight,color,pokedex) values (?,?,?,?,?,?,?,?,?,?,?,?)", (pokemon['id'], pokemon['Name'], pokemon['GenderRate'],pokemon['GrowthRate'],pokemon['Rareness'],pokemon['Happiness'],pokemon['Compatibility'],pokemon['StepsToHatch'],pokemon['Height'],pokemon['Weight'],pokemon['Color'],pokemon['Pokedex']))
            conexion.commit()