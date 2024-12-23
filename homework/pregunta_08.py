"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """

    file = 'files/input/data.csv'
    with open(file, mode='r', newline='', encoding='utf-8') as file:
        lines = file.readlines()
    
    letras = []
    num = {}
    for line in lines:
        columns = line.strip().split('\t')
        if len(columns) > 0:
            letras.append((columns[0],int(columns[1]))) 
    letras = sorted(letras, key=lambda x: x[0])
    
    for letra, valor in letras:
        if valor not in num: 
            num[valor] = [letra]
        else:
            if letra not in num[valor]:
                num[valor].append(letra)
        
    return sorted(num.items())

print(pregunta_08())