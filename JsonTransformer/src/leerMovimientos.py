import json

ficheroJsonMovimientos="movimientos.json"

def leerFicheroMovimientos(ruta,nombreFichero,rutaJson):
    movimientos = {}
    #habilidades[habilidadesId] = habilidad

    with open(ruta+nombreFichero,'r',encoding='utf-8-sig') as f:
        for linea in f:
            linea = linea.replace("\n","")
            lineaSplitAux = linea.split('\"')
            lineaSplit = lineaSplitAux[0].split(',')

            movimientosId = lineaSplit[0]
            nombre = lineaSplit[1]
            nombre_esp = lineaSplit[2]
            potencia = int(lineaSplit[4])
            tipo = lineaSplit[5]
            clase = lineaSplit[6]
            precision = int(lineaSplit[7])
            pp = int(lineaSplit[8])
            descripcion = lineaSplitAux[1].replace("\"","")

            movimientos[movimientosId] = {'nombre':nombre,'nombre_esp':nombre_esp,'potencia':potencia,'tipo':tipo,'clase':clase,'precision':precision,'pp':pp,'descripcion':descripcion}
    

    with open(rutaJson+ficheroJsonMovimientos, "w",encoding='utf-8') as write_file:
        json.dump(movimientos, write_file, indent=4, sort_keys=True,ensure_ascii=False)