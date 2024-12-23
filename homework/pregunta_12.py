"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    file = 'files/input/data.csv'
    with open(file, mode='r', newline='', encoding='utf-8') as file:
        lines = file.readlines()
    
    letras = []
    conteo = {}
    for line in lines:
        columns = line.strip().split('\t')
        if len(columns) > 4:
            trp = columns[4].split(",")
            for value in trp: 
                num = value.split(":")
                letras.append((columns[0], int(num[1])))
    
    for key, val in letras: 
        if key in conteo: 
            conteo[key] += val
        else: 
            conteo[key] = val 
     
    return conteo

print(pregunta_12())