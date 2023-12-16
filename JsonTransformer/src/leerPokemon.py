import json
import re

ficheroJsonPokemon="pokemon.json"

def leerFicheroPokemon(ruta,nombreFichero,rutaJson):
    datos = {}
    datos['pokemons'] = []

    with open(ruta+nombreFichero,'r',encoding='utf-8') as f:
        pokemon = {}
        primerPokemon = True
        for linea in f:
            linea = linea.replace("\n","")
            if '[' in linea:
                if not primerPokemon:
                    datos['pokemons'].append(pokemon)
                    pokemon = {}
                else: 
                    primerPokemon = False
                id = re.sub('[^0-9 \n\.]', '', linea)
                pokemon['id']=id
                print('---------------------')
                print('pokemon id:'+id)
            else:
                lineaSplit = linea.split('=')
                nombre = lineaSplit[0]
                if len(lineaSplit)>1:
                    valor = lineaSplit[1]
                else:
                    valor = ""
                pokemon[nombre]=valor

    with open(rutaJson+ficheroJsonPokemon, "w") as write_file:
        json.dump(datos, write_file, indent=4, sort_keys=True)