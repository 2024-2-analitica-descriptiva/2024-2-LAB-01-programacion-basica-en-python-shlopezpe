"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    file = 'files/input/data.csv'
    with open(file, mode='r', newline='', encoding='utf-8') as file:
        lines = file.readlines()
    
    letras = []
    letras_dict={}
    for line in lines:
        columns = line.strip().split('\t')
        if len(columns) > 0:
            letras.append((columns[0],int(columns[1]))) 
    letras = sorted(letras, key=lambda x: x[0])
    
    
    for letra, valor in letras:
        if letra not in letras_dict:
            letras_dict[letra] = {'max': valor, 'min': valor}
        else:
            letras_dict[letra]['max'] = max(letras_dict[letra]['max'], valor)
            letras_dict[letra]['min'] = min(letras_dict[letra]['min'], valor)
    
    return [(letra, num['max'], num['min']) for letra, num in letras_dict.items()]

print(pregunta_05())