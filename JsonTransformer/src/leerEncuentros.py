import json

ficheroJsonEncuentros="encuentros.json"
ficheroJsonLugares="lugares.json"

ficheroJsonPokemonsId="pokemons_id.json"

def leerFicheroEncuentros(ruta,nombreFichero,rutaJson):
    datos = {}
    datos['encuentros'] = []

    lugares = {}
    lugaresId = 1

    pokemons = {}
    with open(rutaJson+ficheroJsonPokemonsId) as file:
        pokemons = json.load(file) 

    with open(ruta+nombreFichero,'r',encoding='ISO-8859-1') as f:
        nombreEncuentro=""
        lugarId = -1

        for linea in f:
            linea = linea.replace("\n","")
            numAlmohadillas = linea.count('#')
            if numAlmohadillas>1:
                # limpiar variables
                nombreEncuentro=""
                lugarId = -1
            elif numAlmohadillas == 1:
                # id y nombre encuentro
                lineaSplit = linea.split(' # ')
                # no hace falta, el id sera autoincremental
                encuentroId = lineaSplit[0]
                nombreEncuentro = lineaSplit[1]
            elif linea.isalpha():
                # nombre lugar
                if linea not in lugares.values():
                    lugares[lugaresId] = linea
                    lugarId = lugaresId
                    lugaresId += 1
                else:
                    lugarId = list(lugares.keys())[list(lugares.values()).index(linea)]
            else:
                lineaSplit = linea.split(',')
                if not lineaSplit[0].isdigit():
                    pokemon_id = buscarPokemonId(lineaSplit[0],pokemons)
                    nivelMin = lineaSplit[1]
                    if len(lineaSplit) > 2:
                        nivelMax = lineaSplit[2]
                    else:
                        nivelMax = nivelMin
                    datos['encuentros'].append({'pokemon_id':int(pokemon_id),'nombre':nombreEncuentro,'lugar_id':lugarId,'nivel_min':int(nivelMin),'nivel_max':int(nivelMax)})

    with open(rutaJson+ficheroJsonEncuentros, "w",encoding='utf-8') as write_file:
        json.dump(datos, write_file, indent=4, sort_keys=True,ensure_ascii=False)

    with open(rutaJson+ficheroJsonLugares, "w",encoding='utf-8') as write_file:
        json.dump(lugares, write_file, indent=4, sort_keys=True,ensure_ascii=False)
                


def buscarPokemonId(nombrePokemon,pokemons):
    return list(pokemons.keys())[list(pokemons.values()).index(nombrePokemon)]