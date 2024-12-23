"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """

    file = 'files/input/data.csv'
    
    with open(file, mode='r', newline='', encoding='utf-8') as file:
        lines = file.readlines()
        
    fechas = []
    conteo = {}    
    for line in lines:
        columns = line.strip().split('\t')
        if len(columns) > 2:
            mes = columns[2].split("-")[1]
            fechas.append((mes, 1))
    fechas = sorted(fechas, key=lambda x: x[0])
    
    for key, value in fechas: 
        if key in conteo:
            conteo[key] += value
        else:
            conteo[key] = value        
    
    return list(conteo.items())
            
print(pregunta_04())