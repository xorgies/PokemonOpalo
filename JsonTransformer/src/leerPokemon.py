import json
import re

ficheroJsonPokemon="pokemon.json"
ficheroJsonHabilidades="habilidades.json"
ficheroJsonHabilidadesPokemon="habilidades_pokemon.json"
ficheroJsonEstadisticasPokemon="estadisticas_pokemon.json"
ficheroJsonTipos="tipos.json"
ficheroJsonTiposPokemon="tipos_pokemon.json"
ficheroJsonMovimientos="movimientos.json"
ficheroJsonMovimientosPokemon="movimientos_pokemon.json"
ficheroJsonPokemonsId="pokemons_id.json"
ficheroJsonEvolucionesPokemon="evoluciones_pokemon.json"

def leerFicheroPokemon(ruta,nombreFichero,rutaJson):
    datos = {}
    datos['pokemons'] = []

    pokemons = {}

    habilidades = {}
    habilidadesId = 1

    tipos = {}
    tiposId = 1

    movimientos = {}
    movimientosId = 1

    habilidades_pokemon = {}
    habilidades_pokemon['habilidades'] = []

    estadisticas_pokemon = {}
    estadisticas_pokemon['estadisticas'] = []

    tipos_pokemon = {}
    tipos_pokemon['tipos'] = []

    movimientos_pokemon = {}
    movimientos_pokemon['movimientos'] = []

    evoluciones_pokemon = {}
    evoluciones_pokemon['evoluciones'] = []

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

                if 'Abilities' == nombre:
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
                elif 'HiddenAbility' == nombre:
                    if valor not in habilidades.values():
                        habilidades[habilidadesId] = valor
                        habilidadId = habilidadesId
                        habilidadesId = habilidadesId + 1
                    else:
                        habilidadId = list(habilidades.keys())[list(habilidades.values()).index(valor)]
                    habilidades_pokemon['habilidades'].append({'pokemon_id':pokemon_id,'habilidad_id':habilidadId,'tipo':'oculta'})
                elif 'BaseStats' == nombre:
                    baseStatsSplit = valor.split(',')
                    estadisticas_pokemon['estadisticas'].append({'pokemon_id':pokemon_id,'ps':baseStatsSplit[0],'atk':baseStatsSplit[1],'def':baseStatsSplit[2],'spd':baseStatsSplit[3],'atk_sp':baseStatsSplit[4],'def_sp':baseStatsSplit[5]})
                elif 'Type1' == nombre or 'Type2' == nombre:
                    tipoId = -1
                    if valor not in tipos.values():
                        tipos[tiposId] = valor
                        tipoId = tiposId
                        tiposId = tiposId + 1
                    else:
                        tipoId = list(tipos.keys())[list(tipos.values()).index(valor)]
                    tipos_pokemon['tipos'].append({'pokemon_id':pokemon_id,'tipo_id':tipoId})
                elif 'Moves' == nombre:
                    movimientosSplit = valor.split(',')
                    for (nivel, movimiento) in convertirArrayMovimientos(movimientosSplit):
                        movimientoId = -1
                        if movimiento not in movimientos.values():
                            movimientos[movimientosId] = movimiento
                            movimientoId = movimientosId
                            movimientosId = movimientosId + 1
                        else:
                            movimientoId = list(movimientos.keys())[list(movimientos.values()).index(movimiento)]
                        movimientos_pokemon['movimientos'].append({'pokemon_id':pokemon_id,'movimiento_id':movimientoId,'nivel_aprender':int(nivel)})
                elif 'InternalName' == nombre:
                    pokemons[pokemon_id] = valor
                elif 'Evolutions' == nombre:
                    evolucionesSplit = valor.split(',')
                    indiceAux = 1
                    pokemonEvolucion = ''
                    forma = ''
                    descripcion = ''

                    for valorAux in evolucionesSplit:
                        if indiceAux == 1:
                            pokemonEvolucion=valorAux
                            indiceAux += 1
                        elif indiceAux == 2:
                            forma=valorAux
                            indiceAux += 1
                        elif indiceAux == 3:
                            descripcion=valorAux
                            evoluciones_pokemon['evoluciones'].append({'pokemon_id':pokemon_id,'pokemon_evolucion':pokemonEvolucion,'forma':forma,'descripcion':descripcion})
                            indiceAux = 1
                elif 'BaseEXP' not in nombre and 'BattlerAltitude' not in nombre and 'BattlerEnemyY' not in nombre and 'BattlerPlayerY' not in nombre and 'EffortPoints' not in nombre:
                    pokemon[nombre]=valor

    with open(rutaJson+ficheroJsonPokemon, "w",encoding='utf-8') as write_file:
        json.dump(datos, write_file, indent=4, sort_keys=True)

    with open(rutaJson+ficheroJsonHabilidades, "w",encoding='utf-8') as write_file:
        json.dump(habilidades, write_file, indent=4, sort_keys=True)

    with open(rutaJson+ficheroJsonHabilidadesPokemon, "w",encoding='utf-8') as write_file:
        json.dump(habilidades_pokemon, write_file, indent=4, sort_keys=True)

    with open(rutaJson+ficheroJsonEstadisticasPokemon, "w",encoding='utf-8') as write_file:
        json.dump(estadisticas_pokemon, write_file, indent=4, sort_keys=True)

    with open(rutaJson+ficheroJsonTipos, "w",encoding='utf-8') as write_file:
        json.dump(tipos, write_file, indent=4, sort_keys=True)
    
    with open(rutaJson+ficheroJsonTiposPokemon, "w",encoding='utf-8') as write_file:
        json.dump(tipos_pokemon, write_file, indent=4, sort_keys=True)
    
    with open(rutaJson+ficheroJsonMovimientos, "w",encoding='utf-8') as write_file:
        json.dump(movimientos, write_file, indent=4, sort_keys=True)
    
    with open(rutaJson+ficheroJsonMovimientosPokemon, "w",encoding='utf-8') as write_file:
        json.dump(movimientos_pokemon, write_file, indent=4, sort_keys=True)

    with open(rutaJson+ficheroJsonPokemonsId, "w",encoding='utf-8') as write_file:
        json.dump(pokemons, write_file, indent=4, sort_keys=True)

    evoluciones_pokemon = convertirPokemonEvolucionAId(evoluciones_pokemon,pokemons)
    with open(rutaJson+ficheroJsonEvolucionesPokemon, "w",encoding='utf-8') as write_file:
        json.dump(evoluciones_pokemon, write_file, indent=4, sort_keys=True)
    
def convertirArrayMovimientos(array):
    arrayNiveles=[]
    arrayMovimientos=[]
    arrayRespuesta=[]

    for i in array[::2]:
        arrayNiveles.append(i)

    for i in array[1::2]:
        arrayMovimientos.append(i)

    for nivel, movimiento in zip(arrayNiveles, arrayMovimientos):
        arrayRespuesta.append((nivel,movimiento))
    
    return arrayRespuesta

def convertirPokemonEvolucionAId(evoluciones_pokemon,pokemons):
    evoluciones_pokemon_id={}
    evoluciones_pokemon_id['evoluciones']=[]

    for pokemonEvolucion in evoluciones_pokemon['evoluciones']:
        pokemonEvolucionId = list(pokemons.keys())[list(pokemons.values()).index(pokemonEvolucion['pokemon_evolucion'])]
        evoluciones_pokemon_id['evoluciones'].append({'pokemon_id':pokemonEvolucion['pokemon_id'],'pokemon_evolucion_id':int(pokemonEvolucionId),'forma':pokemonEvolucion['forma'],'descripcion':pokemonEvolucion['descripcion']})
    
    return evoluciones_pokemon_id