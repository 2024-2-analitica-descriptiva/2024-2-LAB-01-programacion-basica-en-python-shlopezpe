"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordenadas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    file = 'files/input/data.csv'
    
    with open(file, mode='r', newline='', encoding='utf-8') as file:
        lines = file.readlines()
        
    letras = []
    conteo = {}    
    for line in lines:
        columns = line.strip().split('\t')
        if len(columns) > 0:
            letras.append((columns[0],1)) 
    letras = sorted(letras, key=lambda x: x[0])
    
    for key, value in letras: 
        if key in conteo:
            conteo[key] += value
        else:
            conteo[key] = value        
    

    return list(conteo.items())
            
print(pregunta_02())
