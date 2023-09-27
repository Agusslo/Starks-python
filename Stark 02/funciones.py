from data_stark import lista_personajes

#Agustin Lopez stark 02

def obtener_superheroes_por_genero(lista_personajes, genero):
    """brief: La función busca el genero que le pasen por parametro ya sea F/M/NB
    parametros: personaje lista_personajes  superheroes_por_genero
    return: superheroes_por_genero"""
    superheroes_por_genero = []
    for personaje in lista_personajes:
        if personaje['genero'] == genero:
            superheroes_por_genero.append(personaje)
    return superheroes_por_genero


#A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB
def imprimir_superheroes_genero_NB(lista_personajes):
    """brief: La función itera sobre la lista y muestra todos los heroes genero NB
    parametros: personaje lista_personajes
    return:None  """
    for personaje in lista_personajes:
        if personaje['genero'] == 'NB':
            print(f"\nHeroes con genero NB: {personaje['nombre']}")


#B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
def encontrar_superheroe_mas_alto_genero_F(lista_personajes):
    """brief: La función itera sobre la lista y muestra el heroe mas alto de genero F
    parametros: personaje lista_personajes superheroe_mas_alto altura_actual
    return:None  """
    superheroe_mas_alto = None
    for personaje in lista_personajes:
        if personaje['genero'] == 'F':
            altura_actual = float(personaje['altura'])
            if superheroe_mas_alto is None or altura_actual > float(superheroe_mas_alto['altura']):
                superheroe_mas_alto = personaje
    if superheroe_mas_alto:
        print(f"\nEl superhéroe más alto de género F es: {superheroe_mas_alto['nombre']}")
    else:
        print("No se encontraron superhéroes de género F en la lista.")


#C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
def encontrar_superheroe_mas_alto_genero_M(lista_personajes):
    """brief: La función itera sobre la lista y muestra el heroe mas alto de genero M
    parametros: personaje lista_personajes superheroe_mas_alto altura_actual
    return:None  """
    superheroes_masculinos = obtener_superheroes_por_genero(lista_personajes, 'M')
    superheroe_mas_alto = None
    for personaje in superheroes_masculinos:
        altura_actual = float(personaje['altura'])
        if superheroe_mas_alto is None or altura_actual > float(superheroe_mas_alto['altura']):
            superheroe_mas_alto = personaje
    if superheroe_mas_alto:
        print(f"\nEl superhéroe más alto de género M es: {superheroe_mas_alto['nombre']}")
    else:
        print("No se encontraron superhéroes de género M en la lista.")


#D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
def encontrar_superheroe_mas_debil_genero_M(lista_personajes):
    """brief: La función itera sobre la lista y muestra el heroe mas alto de genero M
    parametros: personaje lista_personajes superheroe_mas_alto altura_actual
    return:None  """
    superheroes_masculinos = obtener_superheroes_por_genero(lista_personajes, 'M')
    superheroe_mas_debil = None
    for personaje in superheroes_masculinos:
        fuerza_actual = float(personaje['fuerza'])
        if superheroe_mas_debil is None or fuerza_actual < float(superheroe_mas_debil['fuerza']):
            superheroe_mas_debil = personaje
    if superheroe_mas_debil:
        print(f"\nEl superhéroe más debil de género M es: {superheroe_mas_debil['nombre']}")
    else:
        print("No se encontraron superhéroes de género M en la lista.")


#E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
def encontrar_superheroe_mas_debil_genero_NB(lista_personajes):
    """brief: La función itera sobre la lista y muestra el heroe mas alto de genero M
    parametros: personaje lista_personajes superheroe_mas_alto altura_actual
    return:None  """
    superheroes_NB = obtener_superheroes_por_genero(lista_personajes, 'NB')
    superheroe_mas_debil = None
    for personaje in superheroes_NB:
        fuerza_actual = float(personaje['fuerza'])
        if superheroe_mas_debil is None or fuerza_actual < float(superheroe_mas_debil['fuerza']):
            superheroe_mas_debil = personaje
    if superheroe_mas_debil:
        print(f"\nEl superhéroe más debil de género NB es: {superheroe_mas_debil['nombre']}")
    else:
        print("No se encontraron superhéroes de género NB en la lista.")


#F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB
def calcular_fuerza_promedio_genero_NB(lista_personajes):
    """brief: La función itera sobre la lista y calcula el promedio de la fuerza de los superhéroes de género NB
    parametros: personaje lista_personajes total_fuerza cantidad_superheroes_NB fuerza_promedio
    return:None  """
    superheroes_NB = obtener_superheroes_por_genero(lista_personajes, 'NB')
    total_fuerza = 0
    cantidad_superheroes_NB = len(superheroes_NB)
    for personaje in superheroes_NB:
        fuerza_actual = int(personaje['fuerza'])
        total_fuerza += fuerza_actual
    if cantidad_superheroes_NB > 0:
        fuerza_promedio = total_fuerza / cantidad_superheroes_NB
        print(f"\nLa fuerza promedio de los superhéroes de género NB es: {fuerza_promedio:.2f}")
    else:
        print("No se encontraron superhéroes de género NB en la lista.")

#G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
def contar_colores_ojos(lista_personajes):
    """brief: La función itera sobre la lista y muestra los tipos de colores de ojo
    parametros: personaje lista_personajes colores_ojos color cantidad color_ojos
    return:None  """
    colores_ojos = {}  
    for personaje in lista_personajes:
        color_ojos = personaje['color_ojos']
        if color_ojos in colores_ojos:
            colores_ojos[color_ojos] += 1
        else:
            colores_ojos[color_ojos] = 1
    for color, cantidad in colores_ojos.items():
        print(f"\nColor de ojos '{color}': {cantidad} superhéroes")


#H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
def contar_colores_pelo(lista_personajes):
    """brief: La función itera sobre la lista y muestra los tipos de colores de pelo
    parametros: personaje lista_personajes colores_pelo color_pelo cantidad color
    return:None  """
    colores_pelo = {} 
    for personaje in lista_personajes:
        color_pelo = personaje['color_pelo']
        if color_pelo in colores_pelo:
            colores_pelo[color_pelo] += 1
        else:
            colores_pelo[color_pelo] = 1
    for color, cantidad in colores_pelo.items():
        print(f"\nColor de pelo '{color}': {cantidad} superhéroes")


#I. Listar todos los superhéroes agrupados por color de ojos.
def listar_superheroes_por_color_ojos(lista_personajes):
    """brief: La función itera sobre la lista y muestra los heroes agrupados por sus ojos
    parametros: personaje lista_personajes colores_pelo color_pelo cantidad color
    return:None  """
    superheroes_por_color_ojos = {} 
    for personaje in lista_personajes:
        nombre = personaje['nombre']
        color_ojos = personaje['color_ojos']
        if color_ojos in superheroes_por_color_ojos:
            superheroes_por_color_ojos[color_ojos].append(nombre)
        else:
            superheroes_por_color_ojos[color_ojos] = [nombre]
    for color, superheroes in superheroes_por_color_ojos.items():
        print(f"\nColor de ojos '{color}': {', '.join(superheroes)}")


#J. Listar todos los superhéroes agrupados por tipo de inteligencia
def listar_superheroes_por_inteligencia(lista_personajes):
    """brief: La función itera sobre la lista y muestra tipos de ingeligencia
    parametros: personaje lista_personajes orden_inteligencia inteligencia nombre superheroes_por_inteligencia
    return:None  """
    orden_inteligencia = ['','high', 'good', 'average']#el orden que aparecen
    superheroes_por_inteligencia = {inteligencia: [] for inteligencia in orden_inteligencia}
    for personaje in lista_personajes:
        inteligencia = personaje["inteligencia"]
        if inteligencia in orden_inteligencia:
            nombre = personaje["nombre"]
            superheroes_por_inteligencia[inteligencia].append(nombre)
    for inteligencia in orden_inteligencia:
        if superheroes_por_inteligencia[inteligencia]:
            print(f"\nTipo de inteligencia '{inteligencia}': {', '.join(superheroes_por_inteligencia[inteligencia])}")