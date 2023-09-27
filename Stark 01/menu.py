"""
A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)
C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo (MÍNIMO)
D. Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)
E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier 
género) los cuales su fuerza supere a la fuerza promedio de todas las
superhéroes de género femenino"""


def mostrar_menu():
    """brief: crea un menu de opciones

    parametros: None

    return:None  """
    for opcion in menu:
        print(opcion)


menu = [
    "\n\n| 1. Lista super heroes",
    "| 2.  Identidad y peso heroe mas fuerte",
    "| 3.  nombre e identidad heroe mas bajo",
    "| 4.  Determinar el peso promedio de los heroes masculinos ",
    "| 5.  Nombre y peso con mas de fuerza promedio de las mujeres",
    "| 0.  Salir del programa",
]
