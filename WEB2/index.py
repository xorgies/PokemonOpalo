from flask import Flask, render_template
import sqlite3
from flask import g

app = Flask(__name__)

###################################################################
# rutas

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calculadora')
def calculadora():
    return render_template('calculadora.html')

@app.route('/pokemonLista')
def lista_pokemon():
    dictPokemon= query_db('select id,name from Pokemon')
    dictPokemon= cambiarFormatoId(dictPokemon,"id")
    dictTipos= aplanarTipos(query_db('select * from pokemon_tipos_view'))
    return render_template('pokemon_lista.html', pokemon=dictPokemon, tipos=dictTipos)

@app.route('/pokemon/<int:pokemon_id>')
def pokemon(pokemon_id):
    dictPokemon= query_db('select * from datos_pokemon_view where id=?',[pokemon_id],one=True)
    generosPorcentaje = calcularGeneros(dictPokemon['genderRate'])
    dictPokemon["male"] = generosPorcentaje[0]
    dictPokemon["female"] = generosPorcentaje[1]
    dictPokemon["id"] = str(dictPokemon["id"]).zfill(3)
    grupos_huevo = str(dictPokemon["compatibility"])
    dictPokemon["compatibility"] = str(dictPokemon["compatibility"]).split(',')
    dictHabilidades= query_db('select * from pokemon_habilidades_view where id=? order by tipo ASC',[pokemon_id])
    dictMovimientos= query_db('select * from pokemon_movimientos_view where id=? order by nivel_aprender ASC',[pokemon_id])
    dictMultiEvo = get_linea_multi_evolutiva(pokemon_id)
    dictPreEvoluciones = []
    dictEvoluciones = []
    if len(dictMultiEvo) <= 1:
        dictMultiEvo = []
        dictPreEvoluciones=  get_linea_pre_evolutiva(pokemon_id)
        dictEvoluciones=  get_linea_evolutiva(pokemon_id)
    dictTipos= query_db('select * from pokemon_tipos_view where id=?',[pokemon_id])
    dictEstadisticasPosicion= get_estadisticas_posicion(dictPokemon)
    dictMovimientosHuevo= query_db('select * from pokemon_movimientos_huevo_view where id=?',[pokemon_id])
    grupos_huevo = grupos_huevo.replace("'","")

    return render_template('pokemon.html', pokemon=dictPokemon, habilidades=dictHabilidades, movimientos=dictMovimientos, multievoluciones=dictMultiEvo, preevoluciones=dictPreEvoluciones, evoluciones=dictEvoluciones, tipos=dictTipos, estadisticasPosicion=dictEstadisticasPosicion, movimientosHuevo=dictMovimientosHuevo, gruposHuevo=grupos_huevo)

@app.route('/group/<string:egg>')
def egg_group(egg):
    egg_group = '%' + egg + '%'
    # TODO: calcular generos y guardarlo en dos nuevas variables (male,female)
    lista_pokemon = query_db('select id,name from Pokemon where compatibility like ?', [egg_group])
    lista_pokemon= cambiarFormatoId(lista_pokemon,"id")
    dictTipos= aplanarTipos(query_db('select * from pokemon_tipos_view'))
    return (render_template('lista_filtrada.html', lista_pokemon=lista_pokemon, titulo=egg, tipos=dictTipos))

@app.route('/tipo/<string:tipo>')
def tipos(tipo):
    tipo_filtro = '%' + tipo + '%'
    lista_tipos = query_db('select distinct id from pokemon_tipos_view where nombre like ?', [tipo_filtro])
    lista_tipos_str = '('
    for entry in lista_tipos:
        lista_tipos_str += str(entry['id'])
        if entry['id'] != lista_tipos[-1]['id']:
            lista_tipos_str += ','
    lista_tipos_str += ')'
    lista_pokemon = query_db('select id, name from Pokemon where id in '+lista_tipos_str)
    tipo = '<img class="img-tipo-filtrado img-center" src="/static/img/tipos/'+tipo+'_xl.png">'
    lista_pokemon= cambiarFormatoId(lista_pokemon,"id")
    dictTipos= aplanarTipos(query_db('select * from pokemon_tipos_view'))
    return render_template('lista_filtrada.html', lista_pokemon=lista_pokemon, titulo=tipo, tipos=dictTipos)

@app.route('/habilidadesLista')
def lista_habilidades():
    dictHabilidades= query_db('select * from Habilidades')
    return render_template('habilidades_lista.html', habilidades=dictHabilidades)

@app.route('/habilidad/<int:habilidad_id>')
def habilidad(habilidad_id):
    dictHabilidad= query_db('select * from Habilidades where id=?',[habilidad_id],one=True)
    dictPokemonsHabilidad= query_db('select * from habilidad_pokemons_view where id=?',[habilidad_id])
    dictPokemonsHabilidad= cambiarFormatoId(dictPokemonsHabilidad,"pokemon_id")
    dictTipos= aplanarTipos(query_db('select * from pokemon_tipos_view'))

    return render_template('habilidad.html', habilidad=dictHabilidad, pokemons=dictPokemonsHabilidad,tipos=dictTipos)

@app.route('/movimientosLista')
def lista_movimientos():
    dictMovimientos= query_db('select * from Movimientos')
    return render_template('movimientos_lista.html', movimientos=dictMovimientos)

@app.route('/movimiento/<int:movimiento_id>')
def movimiento(movimiento_id):
    dictMovimiento= query_db('select * from Movimientos where id=?',[movimiento_id],one=True)
    dictPokemonsHabilidad= query_db('select * from movimiento_pokemons_view where id=?',[movimiento_id])
    dictPokemonsHabilidad= cambiarFormatoId(dictPokemonsHabilidad,"pokemon_id")
    dictTipos= aplanarTipos(query_db('select * from pokemon_tipos_view'))

    return render_template('movimiento.html', movimiento=dictMovimiento, pokemons=dictPokemonsHabilidad,tipos=dictTipos)

@app.route('/movimientoHuevoPadres/<string:nombre_pokemon>/<int:movimiento_id>/<string:grupos_huevo>')
def movimientoHuevoPadre(nombre_pokemon,movimiento_id,grupos_huevo):
    tipo="Padres"
    gruposHuevoWhere = "and ("
    for grupo_huevo in grupos_huevo.split(","):
        gruposHuevoWhere+="p.compatibility like '%%"+grupo_huevo+"%%' or "
    gruposHuevoWhere = gruposHuevoWhere[:-3]
    gruposHuevoWhere +=")"
    lista_pokemon= query_db("""select p.id,p.name,p.compatibility, m.nombre_esp, pm.nivel_aprender 
                                    FROM Pokemon p, Pokemon_Movimientos pm, Movimientos m
                                    WHERE p.id = pm.pokemon_id
                                        and m.id = pm.movimiento_id
                                        and p.genderRate not in ('AlwaysFemale','Genderless')
                                """+gruposHuevoWhere+"""
                                        and m.id = ?
                                UNION
                                select p.id,p.name,p.compatibility, m.nombre_esp, 'egg' as 'nivel_aprender' 
                                FROM Pokemon p, Pokemon_Movimientos_Huevo pmh, Movimientos m
                                WHERE p.id = pmh.pokemon_id
                                    and m.id = pmh.movimiento_id
                                    and p.genderRate not in ('AlwaysFemale','Genderless')
                                """+gruposHuevoWhere+"""
                                    and m.id = ?
                                ORDER BY p.id
                                 """,[movimiento_id,movimiento_id])
    lista_pokemon= cambiarFormatoId(lista_pokemon,"id")
    dictTipos= aplanarTipos(query_db('select * from pokemon_tipos_view'))
    return render_template('movimientoHuevoPadres.html', lista_pokemon=lista_pokemon, titulo=tipo, tipos=dictTipos, nombrePokemon=nombre_pokemon)

@app.route('/encuentros')
def encuentros():
    dictLugares = query_db('select distinct nombre from encuentros_lugares_view')
    cabeceras_tabla = ['Numero', 'Imagen', 'Nombre', 'Tipos', 'Nivel minimo', 'Nivel maximo', 'Lugar de encuentro']
    datos_encuentros = {}
    for lugar in dictLugares:
        lugar = lugar['nombre']
        datos_encuentros[lugar] = []
        lista_pokemon_id = query_db('select distinct pokemon_id from encuentros_lugares_view where nombre = ?', [lugar])
        for pokemon_id in lista_pokemon_id:
            pokemon_id = pokemon_id['pokemon_id']
            lista_lugares_aparicion = query_db('select distinct nombre_lugar from encuentros_lugares_view where nombre = ? and pokemon_id = ?', [lugar, pokemon_id])
            for lugar_aparicion in lista_lugares_aparicion:
                lugar_aparicion = lugar_aparicion['nombre_lugar']
                nivel_min = query_db('select min(nivel_min) as min from encuentros_lugares_view where nombre = ? and pokemon_id = ? and nombre_lugar = ?', [lugar, pokemon_id, lugar_aparicion], True)
                nivel_max = query_db('select max(nivel_max) as max from encuentros_lugares_view where nombre = ? and pokemon_id = ? and nombre_lugar = ?', [lugar, pokemon_id, lugar_aparicion], True)
                dictPokemon= query_db('select id,name from Pokemon where id = ?', [pokemon_id])
                dictPokemon= cambiarFormatoId(dictPokemon,'id')
                dictTipos= query_db('select nombre from pokemon_tipos_view where id = ?', [pokemon_id])
                for pokemon in dictPokemon:
                    pokemon['nivel_min']=nivel_min['min']
                    pokemon['nivel_max']=nivel_max['max']
                    pokemon['lugar_aparicion']=lugar_aparicion
                    tipos = []
                    for tipo in dictTipos:
                        tipos.append(tipo['nombre'])
                    pokemon['tipos'] = tipos
                    datos_encuentros[lugar].append(pokemon)
    print(datos_encuentros['Pueblo Brisa'])
    return render_template('encuentros.html', lugares=dictLugares, cabeceras=cabeceras_tabla, datos=datos_encuentros)

###################################################################
# DATABASE

DATABASE = 'WEB2/static/DB/database.sqlite3'

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = make_dicts
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

# Utils
def get_linea_multi_evolutiva(pokemon_id):
    linea_evolutiva = query_db('select * from evoluciones_view where id=?', [pokemon_id])
    for evolucion in linea_evolutiva:
        evolucion["pokemon_evolucion_id"] = str(evolucion["pokemon_evolucion_id"]).zfill(3)
    return linea_evolutiva

def get_linea_pre_evolutiva(pokemon_id):
    linea_evolutiva=[]
    pokemon = query_db('select * from evoluciones_view where pokemon_evolucion_id=?', [pokemon_id], True)
    if pokemon is not None:
        pokemon["id"] = str(pokemon["id"]).zfill(3)
        linea_evolutiva = get_linea_pre_evolutiva(pokemon["id"])
        linea_evolutiva.append(pokemon)
    return linea_evolutiva

def get_linea_evolutiva(pokemon_id):
    linea_evolutiva=[]
    pokemon = query_db('select * from evoluciones_view where id=?', [pokemon_id], True)
    if pokemon is not None:
        pokemon["pokemon_evolucion_id"] = str(pokemon["pokemon_evolucion_id"]).zfill(3)
        linea_evolutiva.append(pokemon)
        linea_evolutiva.extend(get_linea_evolutiva(pokemon["pokemon_evolucion_id"]))
    return linea_evolutiva

def get_estadisticas_posicion(pokemon):
    estadisticasPosicion = {}
    estadisticas = ['ps','atk','def','spd','atk_sp','def_sp']
    for estadistica in estadisticas:
        queryResult = query_db('select count() as '+estadistica+' from Pokemon p, Pokemon_Estadisticas pe where p.id = pe.pokemon_id and pe.'+estadistica+'>?', [pokemon[estadistica]], True)
        estadisticasPosicion[estadistica] = queryResult[estadistica]
    return estadisticasPosicion

###################################################################
# Utils
def calcularGeneros(genero):
    female = 0
    if 'FemaleOneEighth' == genero:
        female = 12.5
    elif 'Female50Percent' == genero:
        female = 50
    elif 'AlwaysFemale' == genero:
        female = 100
    elif 'AlwaysMale' == genero:
        female = 0
    elif 'Female75Percent' == genero:
        female = 75
    elif 'Female25Percent' == genero:
        female = 25
    
    male = 100 - female
    if 'Genderless' == genero:
        male = 0

    return [male,female]

def cambiarFormatoId(dictPokemon,nombre_id):
    dictPokemonActualizado = []
    for pokemon in dictPokemon:
        pokemon[nombre_id] = str(pokemon[nombre_id]).zfill(3)
        dictPokemonActualizado.append(pokemon)

    return dictPokemonActualizado


def aplanarTipos(tipos):
    tiposPokemon = {}
    for tipo in tipos:
        tipo["id"] = str(tipo["id"]).zfill(3)
        if tipo['id'] not in tiposPokemon.keys():
            tiposPokemon[tipo['id']] = []
        tiposPokemon[tipo['id']].append(tipo['nombre'])

    return tiposPokemon

###################################################################
# Main

if __name__ == '__main__':
    # PRO
    app.run(host='0.0.0.0')

    # Testing
    #app.run(debug=True)
