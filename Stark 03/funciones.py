from os import system
system("cls")
from data_stark import lista_personajes
#Lopez Agustin stark 03

def stark_normalizar_datos(lista: list, key_a_normalizar: str, tipo_de_dato_a_castear):
    """brief: Funcion que toma una lista con diccionarios y 
    castea la key_a_normalizar al tipo de dato que se requiera, puede ser int o float
    parametros: lista key_a_normalizar  dato_a_castear
    return: value"""
    if len(lista) != 0:
        for dato in lista:
            if type(dato[key_a_normalizar]) != int or type(dato[key_a_normalizar]) != float:
                if tipo_de_dato_a_castear == int:
                    dato[key_a_normalizar] = int(
                        dato[key_a_normalizar])
                    value = True
                elif tipo_de_dato_a_castear == float:
                    dato[key_a_normalizar] = float(
                        dato[key_a_normalizar])
                    value = True
            else:
                value = False
    else:
        value = False
    return value


def obtener_dato(lista: list, indice: int, key_a_obtener: str) -> str | int | float:
    """brief: la funcion itera sobre la lista y printea el dato
    parametros: lista indice key_a_obtener 
    return: """
    if len(lista) != 0:
        for dato in lista:
            if key_a_obtener not in dato or key_a_obtener == "nombre" or  lista[indice][key_a_obtener] == '':
                return False
            else:
                    return lista[indice][key_a_obtener]
    else:
        return False



def obtener_nombre(lista: list, indice: int) -> str:
    """brief: la funcion itera sobre la lista y printea el nombre
    parametros: lista indice dato
    return: """
    if len(lista) != 0:
        for dato in lista:
            if "nombre" in dato:
                return f'Nombre: {lista[indice]["nombre"]}'
            else:
                return False
    else:
        return False

def obtener_nombre_y_dato(lista: list, indice: int, key_a_obtener: str) -> str: #2
    """brief: usa las funciones obtener_dato|nombre para printear el nombre y el dato que le pasen
    parametros: heroe nombre dato indice key_a_obtener
    return: heroe nombre dato lista indice key_a_obtener"""
    heroe = {}
    nombre = obtener_nombre(lista, indice)
    dato = obtener_dato(lista, indice, key_a_obtener)
    if dato != False and nombre != False:
        heroe["nombre"] = nombre
        heroe["dato"] = dato
        return heroe
    else:
        return False

def obtener_maximo(lista:list, key_a_obtener:str) -> int or float: #3.1
    """brief: la funcion saca el maximo del dato seleccionado
    parametros: valor_max  dato lista key_a_obtener
    return: valor_max"""
    valor_max = None
    for dato in lista:
        if type(dato[key_a_obtener]) == int or type(dato[key_a_obtener]) == float:
            if valor_max == None:
                valor_max = dato[key_a_obtener]
            elif valor_max < dato[key_a_obtener]:
                valor_max = dato[key_a_obtener]
        else:
            return False
    return valor_max

def obtener_minimo(lista:list, key_a_obtener:str) -> int or float:#3.2
    """brief: la funcion saca el minimo del dato seleccionado
    parametros: valor_min  dato lista key_a_obtener
    return: valor_min"""
    valor_min = None
    for dato in lista:
        if type(dato[key_a_obtener]) == int or type(dato[key_a_obtener]) == float:
            if valor_min == None:
                valor_min = dato[key_a_obtener]
            elif valor_min > dato[key_a_obtener]:
                valor_min = dato[key_a_obtener]
        else:
            return False
    return valor_min

def obtener_dato_cantidad(lista: list, valor_a_comparar:str, key_a_obtener: str) -> list[dict]:#3.3
    """brief: la función filtra una lista de diccionarios para obtener los elementos que coinciden con un valor específico
    en una clave determinada
    parametros: lista_dato dato key_a_obtener valor_a_comparar
    return: lista_dato"""
    lista_dato = []
    for dato in lista:
        if dato[key_a_obtener] == valor_a_comparar:
            lista_dato.append(dato)
    return lista_dato


def stark_imprimir_heroes(lista: list):#3.4
    """brief: la funcion imprime todos los heroes con todos sus datos
    parametros: lista heroe
    return: """
    if len(lista) > 0:
        for heroe in lista:
            print("\n{0}\n".format("―" * 50))
            for clave, valor in heroe.items():
                print("{0}: {1}".format(clave, valor))
    else:
        print(False)

def sumar_dato_heroe(lista: list, key_a_sumar: str) -> int | float:#4.1
    """brief: la funcion suma los datos del dato que le hayan pasado
    parametros: lista key_a_sumar acumulador_dato
    return: acumulador_dato"""
    acumulador_dato = 0
    if len(lista) != 0:
        for dato in lista:
            if key_a_sumar in dato and dato[key_a_sumar] != '' and (type(dato[key_a_sumar]) == int or type(dato[key_a_sumar]) == float):
                acumulador_dato += dato[key_a_sumar]
            else:
                return False
    else:
        return False
    if acumulador_dato == 0:
        return False
    else:
        return acumulador_dato

def dividir (dividendo,divisor):#4.2
    """brief: la funcion realiza la división del dividendo entre el divisor y devuelve el resultado
    parametros: dividendo divisor
    return: """
    if divisor == 0:
        return divisor
    else:
        division = dividendo/divisor
        return division

def calcular_promedio(lista: list, key_a_promediar: str) -> int | float | bool:#4.3
    """brief: la función calcula la suma de ese dato para todos los héroes en la lista y luego divide la suma por la cantidad de héroes 
    para obtener el promedio. 
    parametros: lista key_a_promediar dato_sumado promedio
    return: promedio"""
    dato_sumado = sumar_dato_heroe(lista, key_a_promediar)
    promedio = dividir(dato_sumado, len(lista))
    if dato_sumado != False and promedio != False:
        return promedio
    else:
        return False

def mostrar_promedio_dato(lista: list, key_a_mostar: str) -> str:#4.4
    """brief: la funcion calcula el promedio de los valores correspondientes a esa clave en la lista y devuelve el resultado formateado
    parametros: lista key_a_mostar promedio
    return: f'{promedio:0.2f}' """
    if len(lista) != 0:
        promedio = calcular_promedio(lista, key_a_mostar)
        if promedio == False:
            return False
        else:
            return f'{promedio:0.2f}'
    else:
        return False

def imprimir_menu():#5.1
    """brief: imprime un menu
    parametros: menu 
    return: menu"""
    menu = input("""
1. Normalizar datos
2. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB
3. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
4. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
5. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
6. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
7. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB
8. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
9. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
10. Listar todos los superhéroes agrupados por color de ojos.
11. Listar todos los superhéroes agrupados por tipo de inteligencia
0. SALIR
Ingrese una opción: """)
    return menu.strip() #elimina lo vacio

def validar_entero(numero: str) -> bool:#5.2
    """brief: la funcion valida un entero
    parametros: numero
    return: """
    try:
        int(numero)
        return True
    except ValueError:
        return False

def stark_menu_principal() -> int:#5.3
    """brief: la funcion se encarga de imprimir un menu y valida los numeros que se usaran para seleccionar en el menu
    parametros: valor_input validacion_int
    return: valor_input"""
    while True:
        valor_input = imprimir_menu()
        if valor_input.isdigit():
            option = int(valor_input)
            if 0 <= option <= 11:
                return option
            else:
                print('Ingrese un valor válido (número del 1 al 11).')
        else:
            print('Ingrese un valor válido (número del 1 al 11).') #repito porque si ingresaba otro numero no tiraba mensaje


def stark_marvel_app(lista:list):#6/7
    """brief: 
    parametros: flag valor_input lista lista_genero_nb lista_heroe_femenino heroe_mas_alta_f heroe_mas_altas_f lista_heroe_masculino
    heroe_mas_alto_m heroes_mas_altos_m heroe_mas_debil_m heroes_mas_debiles_m lista_heroe_nb heroe_mas_debil_nb heroes_mas_debiles_nb
    lista_colores_ojos repetidos lista_colores_pelo lista_colores_ojos lista_unica_ojos lista_tipo_inteligencia lista_unica_tipo_inteligencia
    return: None"""
    flag = 0 
    
    while True:
        
        valor_input = stark_menu_principal()
        
        if valor_input == 1 and flag == 0:      
            flag += 1
            print("\nDatos normalizados")
            stark_normalizar_datos(lista, "fuerza", int)#valido los datos
            stark_normalizar_datos(lista, "peso", float)
            stark_normalizar_datos(lista, "altura", float)
        
        
        elif valor_input > 1 and flag == 0:#si o si selecciona opcion 1 primero
            print('\nPrimero debe normalizar los datos.')
        elif valor_input == 1 and flag == 1:
            print("Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente")
    
        elif valor_input == 2 and flag == 1:#B
            lista_genero_nb = obtener_dato_cantidad(lista, "NB", "genero")
            stark_imprimir_heroes(lista_genero_nb)
    
        elif valor_input == 3 and flag == 1:#C
            lista_heroe_femenino = obtener_dato_cantidad(lista, "F", "genero")
            heroe_mas_alta_f = obtener_maximo(lista_heroe_femenino, "altura")
            heroe_mas_altas_f = obtener_dato_cantidad(lista, heroe_mas_alta_f, "altura")
            stark_imprimir_heroes(heroe_mas_altas_f)
    
        elif valor_input == 4 and flag == 1:#D
            lista_heroe_masculino = obtener_dato_cantidad(lista, "M", "genero")
            heroe_mas_alto_m = obtener_maximo(lista_heroe_masculino, "altura")
            heroes_mas_altos_m = obtener_dato_cantidad(lista, heroe_mas_alto_m, "altura")
            stark_imprimir_heroes(heroes_mas_altos_m)
    
        elif valor_input == 5 and flag == 1:#E
            lista_heroe_masculino= obtener_dato_cantidad(lista, "M", "genero")
            heroe_mas_debil_m = obtener_minimo(lista_heroe_masculino, "fuerza")
            heroes_mas_debiles_m = obtener_dato_cantidad(lista, heroe_mas_debil_m, "fuerza")
            stark_imprimir_heroes(heroes_mas_debiles_m)
    
        elif valor_input == 6 and flag == 1:#F
                lista_heroe_nb = obtener_dato_cantidad(lista, "NB", "genero")
                heroe_mas_debil_nb = obtener_minimo(lista_heroe_nb, "fuerza")
                heroes_mas_debiles_nb = obtener_dato_cantidad(lista, heroe_mas_debil_nb, "fuerza")
                stark_imprimir_heroes(heroes_mas_debiles_nb)
        
        elif valor_input == 7 and flag == 1:#G
            lista_heroe_nb = obtener_dato_cantidad(lista, "NB", "genero")
            print(f'\nEl promedio de fuerza del genero no binario es: {mostrar_promedio_dato(lista_heroe_nb, "fuerza")}')
        
        elif valor_input == 8 and flag == 1:#H
            lista_colores_ojos = []
            repetidos = {}
            for i in range(len(lista)):
                lista_colores_ojos.append(obtener_dato(lista,i, "color_ojos").capitalize())
            for valor in lista_colores_ojos:
                if valor in repetidos:
                    repetidos[valor] += 1
                else:
                    repetidos[valor] = 1
            resultado = []
            for key in repetidos:
                repetidos[key] += 1
                resultado.append(key)
            for repetido in resultado:
                print(f' {repetido} : {repetidos[repetido]}')
    
        elif valor_input == 9 and flag == 1:#I
            lista_colores_pelo = []
            repetidos = {} 
            for i in range(len(lista)): #itero sobre todos los colores con el i y los meto en lista_colores_pelo
                lista_colores_pelo.append(obtener_dato(lista,i, "color_pelo"))
            for valor in lista_colores_pelo:
                if valor == '' or valor == 'No Hair' or valor == False:
                    valor = 'Sin pelo'
                if valor in repetidos:
                    repetidos[valor] += 1
                else:
                    repetidos[valor] = 1
            resultado = []
            for key in repetidos:
                repetidos[key] += 1
                resultado.append(key)
            for repetido in resultado:
                print(f' {repetido} : {repetidos[repetido]}')   
    
        elif valor_input == 10 and flag == 1:#J
            lista_colores_ojos = []
            lista_unica_ojos = []
            for i in range(len(lista)):
                valor = obtener_dato(lista, i , "color_ojos").capitalize()
                lista_colores_ojos.append(valor)
            colores_sin_repetir = set(lista_colores_ojos)
            for color in colores_sin_repetir:
                lista_unica_ojos.append(color)
            for indice in range(len(lista_unica_ojos)):
                for i in range(len(lista_colores_ojos)):
                    if lista_unica_ojos[indice] == lista_colores_ojos[i]:
                        valor = obtener_nombre_y_dato(lista, i, "color_ojos")
                        print('{0} | {1}'.format(valor["nombre"], valor["dato"]))
    
        elif valor_input == 11 and flag == 1:#K
            lista_tipo_inteligencia = []
            lista_unica_tipo_inteligencia = []
            for i in range(len(lista)):
                valor = obtener_dato(lista, i , "inteligencia")
                if valor == False:
                    valor = "Sin inteligencia"
                valor = valor.capitalize()
                lista_tipo_inteligencia.append(valor)
            colores_sin_repetir = set(lista_tipo_inteligencia)
            for color in colores_sin_repetir:
                lista_unica_tipo_inteligencia.append(color)
            for indice in range(len(lista_unica_tipo_inteligencia)):
                for i in range(len(lista_tipo_inteligencia)):
                    if lista_unica_tipo_inteligencia[indice] == lista_tipo_inteligencia[i]:
                        valor = obtener_nombre_y_dato(lista, i, "inteligencia")
                        if type(valor) == bool:
                            pass
                        else:
                            print('{0} | {1}'.format(valor["nombre"], valor["dato"]))
    
        elif valor_input == 0 and flag >= 0:
            print('¡Gracias por usar el programa! nos vemos en la proxima ♥♥♥')
            break
        else:
            print('Ingrese un valor valido')
stark_marvel_app(lista_personajes)