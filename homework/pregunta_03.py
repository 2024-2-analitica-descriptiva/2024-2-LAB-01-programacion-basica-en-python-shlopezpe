"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    file = 'files/input/data.csv'
    with open(file, mode='r', newline='', encoding='utf-8') as file:
        lines = file.readlines()
    
    letras = []
    conteo = {}    
    for line in lines:
        columns = line.strip().split('\t')
        if len(columns) > 0:
            letras.append((columns[0],int(columns[1]))) 
    letras = sorted(letras, key=lambda x: x[0])
    
    for key, value in letras: 
        if key in conteo:
            conteo[key] += value
        else:
            conteo[key] = value        
    

    return list(conteo.items())
            
print(pregunta_03())