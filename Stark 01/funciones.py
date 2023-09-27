from data_stark import lista_personajes

#Agustin Lopez Stark 01

def obtener_superheroes_por_genero(lista_personajes, genero):
    """brief: La función busca el genero que le pasen por parametro ya sea F/M/NB
    parametros: personaje lista_personajes  superheroes_por_genero
    return: superheroes_por_genero"""
    superheroes_por_genero = []
    for personaje in lista_personajes:
        if personaje['genero'] == genero:
            superheroes_por_genero.append(personaje)
    return superheroes_por_genero

#A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
def mostrar_heroes(lista_personajes):
    """brief: La función itera sobre la lista y muestra los datos ordenados
    parametros: personaje lista_personajes  
    return: None"""
    print('NOMBRE          EMPRESA         ALTURA  PESO  GENERO    COLOR DE OJOS  COLOR DE PELO   FUERZA          IDENTIDAD')
    for personaje in lista_personajes:
        print(f"{personaje['nombre']:18} {personaje['empresa']:10}    {float(personaje['altura']):.0f}     {float(personaje['peso']):.0f}      {personaje['genero']:4}    {personaje['color_ojos']:6}          {personaje ['color_pelo']:6}         {personaje['fuerza']:3} {personaje['inteligencia']:10} {personaje['identidad']:10} ")


#B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)
def mostrar_superheroe_mas_fuerte(lista_personajes):
    """brief: La función itera sobre la lista y muestra el personaje mas fuerte
    parametros: e_fuerza lista_personajes mayor_fuerza flag
    return: None"""
    mayor_fuerza = lista_personajes[0]
    flag = False
    for e_fuerza in lista_personajes:
        if int(e_fuerza['fuerza']) > int(mayor_fuerza['fuerza']) or flag == False:
            mayor_fuerza = e_fuerza
            flag = True
    print("\nEl héroe más fuerte es {0} con un peso de {1:.0f}".format(mayor_fuerza['identidad'], float(mayor_fuerza['peso'])))





#C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo(MÍNIMO)
def mostrar_superheroe_mas_bajo(lista_personajes):
    """brief: La función itera sobre la lista y muestra el heroe mas bajo
    parametros: personaje lista_personajes superheroe_mas_bajo
    return: None"""
    superheroe_mas_bajo = None
    for personaje in lista_personajes:
        if superheroe_mas_bajo is None or personaje['altura'] < superheroe_mas_bajo["altura"]:
            superheroe_mas_bajo = personaje
    if superheroe_mas_bajo:
        print("\n\nSuperhéroe más bajo:")
        print("Nombre:", superheroe_mas_bajo['nombre'])
        print("Identidad:", superheroe_mas_bajo['identidad'])
    else:
        print("No se encontró ningún superhéroe.")


#D. Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)
def peso_promedio_superheroes_masculinos(lista_personajes):
    """brief: La función itera sobre la lista y calcula el promedio de héroes masculinos
    parametros: personaje lista_personajes contador_superheroes_masculinos suma_pesos_superheroes_masculinos peso_promedio
    return: None"""
    superheroes_masculinos = obtener_superheroes_por_genero(lista_personajes, 'M')
    contador_superheroes_masculinos = 0
    suma_pesos_superheroes_masculinos = 0
    for personaje in superheroes_masculinos:
        contador_superheroes_masculinos += 1
        suma_pesos_superheroes_masculinos += float(personaje['peso'])
    if contador_superheroes_masculinos == 0:
        print("No hay superhéroes masculinos en la lista.")
    else:
        peso_promedio = suma_pesos_superheroes_masculinos / contador_superheroes_masculinos
        print("\n\nPeso promedio de superhéroes masculinos: {:.2f}".format(peso_promedio))


'''E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género) 
los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino'''

def mostrar_superheroes_fuerza_superior_promedio_femenino(lista_personajes):
    """brief: La función itera sobre la lista y muestre los heroes con mas fuerza promedio del genero F
    parametros: personaje lista_personajes suma_fuerza_femenino contador_femenino fuerza_promedio_femenino
    return: None"""
    suma_fuerza_femenino = 0
    contador_femenino = 0
    for personaje in lista_personajes:
        if personaje['genero'] == 'F': #error con la funcion obtener_superheroes_por_genero, no muestra todos los heroes
            contador_femenino += 1
            suma_fuerza_femenino += int(personaje["fuerza"])#pasamos la fuerza a int(ya que es un texto)
    if contador_femenino == 0:
        print("No hay superhéroes de género femenino en la lista.")
        return

    fuerza_promedio_femenino = suma_fuerza_femenino / contador_femenino
    print("Superhéroes con fuerza superior al promedio femenino:\n")
    print('NOMBRE              PESO')
    for personaje in lista_personajes:
        fuerza_personaje = int(personaje['fuerza'])
        if fuerza_personaje > fuerza_promedio_femenino:
            print(f"{personaje['nombre']:18}  {float(personaje['peso']):.0f} ")




