"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

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
            for code in trp: 
                tup = code.split(":")
                letras.append ((tup[0], 1))
    letras = sorted(letras, key=lambda x: x[0])

    for key, value in letras: 
        if key in conteo:
            conteo[key]+= value
        else:
            conteo[key] = value
    return conteo

print(pregunta_09())