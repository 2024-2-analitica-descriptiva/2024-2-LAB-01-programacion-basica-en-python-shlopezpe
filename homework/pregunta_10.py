"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """

    file = 'files/input/data.csv'
    
    with open(file, mode='r', newline='', encoding='utf-8') as file:
        lines = file.readlines()
        
    
    letras = []
    for line in lines:
        columns = line.strip().split('\t')
        if len(columns) > 0:
            letra = columns[0]
            lt_c = len(columns[3].split(","))
            code = len(columns[4].split(","))
            letras.append((letra,lt_c,code))
    return letras
    
print(pregunta_10())