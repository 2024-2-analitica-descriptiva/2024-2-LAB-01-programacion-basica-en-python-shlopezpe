"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    file = 'files/input/data.csv'
    
    with open(file, mode='r', newline='', encoding='utf-8') as file:
        lines = file.readlines()
        
    letras = []
    conteo = {}    
    for line in lines:
        columns = line.strip().split('\t')
        if len(columns) > 0:
            sep = columns[3].split(",")
            for letra in sep: 
                letras.append((letra,int(columns[1]))) 
    letras = sorted(letras, key=lambda x: x[0])
    
    for key, value in letras: 
        if key in conteo:
            conteo[key] += value
        else:
            conteo[key] = value        
    

    return conteo
            
print(pregunta_11())
