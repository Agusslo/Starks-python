from funciones import *
from menu import *
from os import system
system("cls")

seguir = True

while seguir:
    mostrar_menu()
    try:
        respuesta = int(input("Ingrese Una Opcion: "))
        match respuesta:
            case 1:
                mostrar_heroes(lista_personajes)#A
            case 2:
                mostrar_superheroe_mas_fuerte(lista_personajes)#B
            case 3:
                mostrar_superheroe_mas_bajo(lista_personajes)#C
            case 4:
                peso_promedio_superheroes_masculinos(lista_personajes)#D
            case 5:
                mostrar_superheroes_fuerza_superior_promedio_femenino(lista_personajes)#E
            case 0:
                seguir = False
    except ValueError:
        print("ERROR, NO INGRESO UN VALOR ENTERO")
