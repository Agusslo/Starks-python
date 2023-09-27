from os import system
system("cls")

from funciones import *
from menu import *


seguir = True

while seguir:
    mostrar_menu()
    try:
        respuesta = int(input("Ingrese Una Opcion: "))
        match respuesta:
            case 1:
                imprimir_superheroes_genero_NB(lista_personajes)#A
            case 2:
                encontrar_superheroe_mas_alto_genero_F(lista_personajes)#B
            case 3:
                encontrar_superheroe_mas_alto_genero_M(lista_personajes)#C
            case 4:
                encontrar_superheroe_mas_debil_genero_M(lista_personajes)#D
            case 5:
                encontrar_superheroe_mas_debil_genero_NB(lista_personajes)#E
            case 6:
                calcular_fuerza_promedio_genero_NB(lista_personajes)#F
            case 7:
                contar_colores_ojos(lista_personajes)#G
            case 8:
                contar_colores_pelo(lista_personajes)#H
            case 9:
                listar_superheroes_por_color_ojos(lista_personajes)#I
            case 10:
                listar_superheroes_por_inteligencia(lista_personajes)#J
            case 0:
                seguir = False
    except ValueError:
        print("ERROR, NO INGRESO UN VALOR ENTERO")
