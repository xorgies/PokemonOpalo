import json
import re

ficheroJsonPokemon="pokemon.json"
ficheroJsonHabilidades="habilidades.json"
ficheroJsonHabilidadesPokemon="habilidades_pokemon.json"

def leerFicheroPokemon(ruta,nombreFichero,rutaJson):
    datos = {}
    datos['pokemons'] = []

    habilidades = {}
    habilidadesId = 1

    habilidades_pokemon = {}
    habilidades_pokemon['habilidades'] = []

    with open(ruta+nombreFichero,'r',encoding='utf-8') as f:
        pokemon = {}
        id_pokemon=-1

        primerPokemon = True
        for linea in f:
            linea = linea.replace("\n","")
            if '[' in linea:
                if not primerPokemon:
                    datos['pokemons'].append(pokemon)
                    pokemon = {}
                else: 
                    primerPokemon = False
                id = int(re.sub('[^0-9 \n\.]', '', linea))
                pokemon_id = id
                pokemon['id']=id
                print('---------------------')
                print('pokemon id:'+str(id))
            else:
                lineaSplit = linea.split('=')
                nombre = lineaSplit[0]
                if len(lineaSplit)>1:
                    valor = lineaSplit[1]
                else:
                    valor = ""

                if 'Abilities' in nombre:
                    habilidadesSplit = valor.split(',')
                    for habilidad in habilidadesSplit:
                        habilidadId = -1
                        if habilidad not in habilidades.values():
                            habilidades[habilidadesId] = habilidad
                            habilidadId = habilidadesId
                            habilidadesId = habilidadesId + 1
                        else:
                            habilidadId = list(habilidades.keys())[list(habilidades.values()).index(habilidad)]
                        habilidades_pokemon['habilidades'].append({'pokemon_id':pokemon_id,'habilidad_id':habilidadId,'tipo':'normal'})
                elif 'HiddenAbility' in nombre:
                    if valor not in habilidades.values():
                        habilidades[habilidadesId] = valor
                        habilidadId = habilidadesId
                        habilidadesId = habilidadesId + 1
                    else:
                        habilidadId = list(habilidades.keys())[list(habilidades.values()).index(valor)]
                    habilidades_pokemon['habilidades'].append({'pokemon_id':pokemon_id,'habilidad_id':habilidadId,'tipo':'oculta'})
                pokemon[nombre]=valor

    with open(rutaJson+ficheroJsonPokemon, "w",encoding='utf-8') as write_file:
        json.dump(datos, write_file, indent=4, sort_keys=True)

    with open(rutaJson+ficheroJsonHabilidades, "w",encoding='utf-8') as write_file:
        json.dump(habilidades, write_file, indent=4, sort_keys=True)

    with open(rutaJson+ficheroJsonHabilidadesPokemon, "w",encoding='utf-8') as write_file:
        json.dump(habilidades_pokemon, write_file, indent=4, sort_keys=True)
