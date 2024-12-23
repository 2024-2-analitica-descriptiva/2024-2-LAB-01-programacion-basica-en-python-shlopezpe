"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    file = 'files/input/data.csv'
    with open(file, mode='r', newline='', encoding='utf-8') as file:
        lines = file.readlines()
    
    letras = []
    letras_dict={}
    for line in lines:
        columns = line.strip().split('\t')
        if len(columns) > 4:
            trp = columns[4].split(",")
            for code in trp: 
                tup = code.split(":")
                letras.append((tup[0],int(tup[1]))) 
    letras = sorted(letras, key=lambda x: x[0])
    
    
    for letra, valor in letras:
        if letra not in letras_dict:
            letras_dict[letra] = {'max': valor, 'min': valor}
        else:
            letras_dict[letra]['max'] = max(letras_dict[letra]['max'], valor)
            letras_dict[letra]['min'] = min(letras_dict[letra]['min'], valor)
    
    return [(letra, num['min'], num['max']) for letra, num in letras_dict.items()]

print(pregunta_06())