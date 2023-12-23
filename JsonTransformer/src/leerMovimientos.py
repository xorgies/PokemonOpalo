import json

ficheroJsonMovimientos="movimientos.json"

def leerFicheroMovimientos(ruta,nombreFichero,rutaJson):
    movimientos = {}
    #habilidades[habilidadesId] = habilidad

    with open(ruta+nombreFichero,'r',encoding='utf-8-sig') as f:
        for linea in f:
            linea = linea.replace("\n","")
            lineaSplit = linea.split(',')

            movimientosId = lineaSplit[0]
            nombre = lineaSplit[1]
            nombre_esp = lineaSplit[2]
            potencia = int(lineaSplit[4])
            tipo = lineaSplit[5]
            clase = lineaSplit[6]
            precision = int(lineaSplit[7])
            pp = int(lineaSplit[8])
            descripcion = lineaSplit[13]

            movimientos[movimientosId] = {'nombre':nombre,'nombre_esp':nombre_esp,'potencia':potencia,'tipo':tipo,'clase':clase,'precision':precision,'pp':pp,'descripcion':descripcion.replace("\"","")}
    

    with open(rutaJson+ficheroJsonMovimientos, "w",encoding='utf-8') as write_file:
        json.dump(movimientos, write_file, indent=4, sort_keys=True,ensure_ascii=False)