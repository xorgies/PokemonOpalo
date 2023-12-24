import json

ficheroJsonHabilidades="habilidades.json"

def leerFicheroHabilidades(ruta,nombreFichero,rutaJson):
    habilidades = {}
    #habilidades[habilidadesId] = habilidad

    with open(ruta+nombreFichero,'r',encoding='utf-8-sig') as f:
        for linea in f:
            linea = linea.replace("\n","")
            lineaSplitAux = linea.split('\"')
            lineaSplit = lineaSplitAux[0].split(',')

            habilidadesId = lineaSplit[0]
            nombre = lineaSplit[1]
            nombre_esp = lineaSplit[2]
            descripcion = lineaSplitAux[1].replace("\"","")


            habilidades[habilidadesId] = {'nombre':nombre,'nombre_esp':nombre_esp,'descripcion':descripcion}
    

    with open(rutaJson+ficheroJsonHabilidades, "w",encoding='utf-8') as write_file:
        json.dump(habilidades, write_file, indent=4, sort_keys=True,ensure_ascii=False)