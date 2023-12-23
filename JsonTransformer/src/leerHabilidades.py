import json

ficheroJsonHabilidades="habilidades.json"

def leerFicheroHabilidades(ruta,nombreFichero,rutaJson):
    habilidades = {}
    #habilidades[habilidadesId] = habilidad

    with open(ruta+nombreFichero,'r',encoding='utf-8-sig') as f:
        for linea in f:
            linea = linea.replace("\n","")
            lineaSplit = linea.split(',')

            habilidadesId = lineaSplit[0]
            nombre = lineaSplit[1]
            nombre_esp = lineaSplit[2]
            descripcion = lineaSplit[3]


            habilidades[habilidadesId] = {'nombre':nombre,'nombre_esp':nombre_esp,'descripcion':descripcion.replace("\"","")}
    

    with open(rutaJson+ficheroJsonHabilidades, "w",encoding='utf-8') as write_file:
        json.dump(habilidades, write_file, indent=4, sort_keys=True,ensure_ascii=False)