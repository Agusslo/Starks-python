"""
A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB
B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB
G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
I. Listar todos los superhéroes agrupados por color de ojos.
J. Listar todos los superhéroes agrupados por tipo de inteligencia"""


def mostrar_menu():
    """brief: crea un menu de opciones

    parametros: None

    return:None  """
    for opcion in menu:
        print(opcion)


menu = [
    "\n\n| 1. Superhéroes con el genero NB",
    "| 2.  Superhéroe mas alto de genero F",
    "| 3.  Superhéroe mas alto de genero M",
    "| 4.  Superhéroe mas debil de genero M",
    "| 5.  Superhéroe mas debil de genero NB",
    "| 6.  Fuerza promedio superheroes de genero NB",
    "| 7.  Cantidad de color de ojos",
    "| 8.  Cantidad de color de pelo",
    "| 9.  Lista superheroe agrupado por color de ojos",
    "| 10. Lista superheroe agrupado por tipo de inteligencia",
    "| 0.  Salir",
]
