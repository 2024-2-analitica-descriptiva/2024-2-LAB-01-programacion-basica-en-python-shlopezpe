"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214
    """
#Leer archivo
    file = 'files/input/data.csv'

    with open(file, mode='r', newline='', encoding='utf-8') as file:
        lines = file.readlines()
    
    total_sum = 0
    for line in lines:
        columns = line.strip().split('\t')
        if len(columns) > 1:
            try:
                total_sum += int(columns[1])
            except ValueError:
                pass
    
    return total_sum

print(pregunta_01())
