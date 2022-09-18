"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """
from email import header
from unittest import result
from wsgiref import headers
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from tabulate import tabulate
assert cf

default_limit = 1000
sys.setrecursionlimit(default_limit*100)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def newController(dataStructure):
    """
    Se crea una instancia del controlador
    """
    control = controller.newController(dataStructure)
    return control
sizeDatos = "p"
def tamanoDeMuestra():
    print("Selecciones el tamaño de la muestra")
    print("1- small")
    print("2- 5pct")
    print("3- 10pct")
    print("4- 20pct")
    print("5- 30pct")
    print("6- 50pct")
    print("7- 80pct")
    print("8- large")
    tamano = input()
    file = ""
    if int(tamano) == 1:
        file = "_titles-utf8-small.csv"
        sizeDatos = "muestra pequeña"
    elif int(tamano) == 2:
        file = "_titles-utf8-5pct.csv"
        sizeDatos = "5%"
    elif int(tamano) == 3:
        file = "_titles-utf8-10pct.csv"
        sizeDatos = "10%"
    elif int(tamano) == 4:
        file = "_titles-utf8-20pct.csv"
        sizeDatos = "20%"
    elif int(tamano) == 5:
        file = "_titles-utf8-30pct.csv"
        sizeDatos = "30%"
    elif int(tamano) == 6:
        file = "_titles-utf8-50pct.csv"
        sizeDatos = "50%"
    elif int(tamano) == 7:
        file = "_titles-utf8-80pct.csv"
        sizeDatos = "80%"
    elif int(tamano) == 8:
        file = "_titles-utf8-large.csv"
        sizeDatos = "muestra grande"
    else:
        print("Opción no valida")
    return file, sizeDatos



def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar las películas estrenadas en un periodo")
    print("3- Listar programas de televisión agregados en un periodo de tiempo")
    print("4- Encontrar contenido donde participa un actor")
    print("5- Encontrar contenido por un género especifico")
    print("6- Encontrar contenido producido en un país")
    print("7- Encontrar contenido con un director involucrado")
    print("8- Listar el TOP (N) de los géneros con más contenido")
    #print("9- Listar el TOP (N) de los actores con más participaciones en contenido")
    print("9- Ordenar por fecha de lanzamiento")
    print("10- Elegír la estructura de datos")

def loadData(control, file):
    """
    Solicita al controlador que cargue los datos en el modelo
    """
    amazon_prime, disney_plus, hulu, netflix = controller.loadData(control, file)
    return amazon_prime, disney_plus, hulu, netflix

def dataStructure(dt:int):
    if dt == 1:
        tad = "SINGLE_LINKED"
    elif dt == 2:
        tad = "ARRAY_LIST"
    return tad

control = newController("ARRAY_LIST")
dt = 2




"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs) == 1:
        tad = dataStructure(dt)
        control = newController(tad)
        file = tamanoDeMuestra()
        sizeDatos = file[1]
        file = file[0]


        print("Cargando información de los archivos ....")
        print("Estructura de Datos Utilizada")
        print(control["model"]["hulu"]["type"])
        print()
        amazon_prime, disney_plus, hulu, netflix = loadData(control, file)
        nombre_servicios_streaming = [("Amazon Prime", amazon_prime),
                                     ("Disney Plus", disney_plus),
                                     ("Hulu", hulu),
                                     ("Netflix",netflix)]
        rslt = {"Servicio": [], "N-Registros": [] }
        f_three = {"Servicio": [], "Nombre": [], "Año": [], "Duracion": [], "Clasificacion": []}
        l_three = {"Servicio": [], "Nombre": [], "Año": [], "Duracion": [], "Clasificacion": []}
        for servicios in nombre_servicios_streaming:
            name_servicio, inf_servicio = servicios
            tot_cont, first_three, last_three = inf_servicio

            rslt["Servicio"].append(name_servicio)
            rslt["N-Registros"].append(str(tot_cont))
            for titles in lt.iterator(first_three):
                name = str(titles["title"])
                año_publicacion = str(titles["release_year"])
                duracion = str(titles["duration"])
                clasificacion = str(titles["rating"])
                f_three["Servicio"].append(name_servicio)
                f_three["Nombre"].append(name)
                f_three["Año"].append(año_publicacion)
                f_three["Duracion"].append(duracion)
                f_three["Clasificacion"].append(clasificacion)
            
            for titles in lt.iterator(last_three):
                name = str(titles["title"])
                año_publicacion = str(titles["release_year"])
                duracion = str(titles["duration"])
                clasificacion = str(titles["rating"])

                l_three["Servicio"].append(name_servicio)
                l_three["Nombre"].append(name)
                l_three["Año"].append(año_publicacion)
                l_three["Duracion"].append(duracion)
                l_three["Clasificacion"].append(clasificacion)

        header_titles = ["Servicio", "Titulo", "Año de Lanzamiento", "Duración", "Clasificación"]
        print(tabulate(rslt, headers=["Servicio", "No. de registros cargados"]))
        print("\nPrimeros 3 registros\n")
        print(tabulate(f_three, headers=header_titles, tablefmt="grid"))
        print("\nÚltimos 3 registros\n")
        print(tabulate(l_three, headers=header_titles, tablefmt="grid"))
        
    
    elif int(inputs[0]) == 2:
        lim_inf= int(input("introduzca el limite inferior para el que quiere buscar las peliculas: "))
        lim_sup= int(input("introduzca el limite superior para el que quiere buscar las peliculas: "))
        print("Buscando ....")
    #    peliculas= controller.listar_peliculas_estrenadas_en un periodo(lim_inf,lim_sup)
    #    print(peliculas)

    elif int(inputs[0]) == 3:
        fecha_inicial= input("introduzca la fecha inicial, con formato: %B %d, %Y : ")
        fecha_final= input("introduzca la fecha final, con formato: %B %d, %Y : ")
        print("Buscando....")
    #    programas= controller.listar_programas_agregados en un periodo(fecha_inicial,fecha_final)
    # print(programas)

    elif int(inputs[0]) == 4:
        nombre_actor= input("introduzca el nombre del autor que desea consultar: ")
        print("Buscando ....")
    #    contenido_actor= controller.encontrar_contenido_x_actor(nombre_actor)
    #   print(contenido_actor)

    elif int(inputs[0]) == 5:
        genero= input("introduzca el genero que desea buscar: ")
        print("Buscando ....")
    #    contenido_genero= controller.encontrar_contenido_x_genero(genero)
    # print(contenido_genero)

    elif int(inputs[0]) == 6:
        pais= input("introduzca el pais a consultar: ")
        print("Buscando ....")
    #    contenido_pais= controller.contenido_x_pais(pais)
    #   print(contenido_pais) 

    elif int(inputs[0]) == 7:
        director= input("introduzca el director a consultar")
        print("Buscando ....")
    #    contenido_x_director= controller.contenido_x_director(director)
    # print(contenido_x_director)1

    elif int(inputs[0]) == 8:
        n= int(input("ingrese el numero n de top generos que quiere buscar"))
        print("Buscando ....")
    #    top_n_generos= controller.top_n_generos(n)
    # print(top_n_generos)

    # elif int(inputs[0]) == 9:
    #     n= int(input("introduzca el n top de actores que desea consultar"))
    #     print("Buscando ....")
    elif int(inputs[0]) == 9:
        print("Eliga el algoritmo de ordenamiento")
        print("1- Selection Sort")
        print("2- Insertion Sort")
        print("3- Shell Sort ")
        print("4- Quick Sort")
        print("5- Merge Sort")

        sort = input()
        time = controller.sortTitles(control, sort)
        time = f"{time[1]:.3f}"
        print("Para ordenar "+ sizeDatos + " de todos los datos se demoró ", str(time))

    elif int(inputs) == 10:
        print("Eliga en qué tipo de estructura de datos desea cargar los datos")
        print("1- Lista encadenada")
        print("2- Array")
        dt = int(input())
        
    # top_n_actores= controller.top_n_actores(n)
    # print(top_n_actores)

    elif int(inputs[0]) == 0:
        sys.exit(0)

    else:
        continue
sys.exit(0)