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
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def newController():
    """
    Se crea una instancia del controlador
    """
    control = controller.newController()
    return control

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
    print("9- Listar el TOP (N) de los actores con más participaciones en contenido")

def loadData(control):
    """
    Solicita al controlador que cargue los datos en el modelo
    """
    amazon_prime, disney_plus, hulu, netflix = controller.loadData(control)
    return amazon_prime, disney_plus, hulu, netflix

control = newController()

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        amazon_prime, disney_plus, hulu, netflix = loadData(control)
        nombre_servicios_streaming = [("Amazon Prime", amazon_prime),
                                     ("Disney Plus", disney_plus),
                                     ("Hulu", hulu),
                                     ("Netflix",netflix)]

        for servicios in nombre_servicios_streaming:
            name_servicio, inf_servicio = servicios
            tot_cont, first_three, last_three = inf_servicio

            print(name_servicio+": ")
            print("Total de Contenido Registrado: "+str(tot_cont))
            print("Primeros 3 Contenidos Registrados (Año Publicación, Duración y Clasificación): ")
            for titles in first_three:
                name = str(titles["nombre"])
                año_publicacion = str(titles["año de publicación"])
                duracion = str(titles["duración"])
                clasificacion = str(titles["clasificación"])
                print(name+" ("+año_publicacion+", "+duracion+", "+clasificacion)

            print("Ultimos 3 Contenidos Registrados (Año Publicación, Duración y Clasificación): ")
            for titles in last_three:
                name = str(titles["nombre"])
                año_publicacion = str(titles["año de publicación"])
                duracion = str(titles["duración"])
                clasificacion = str(titles["clasificación"])
                print(name+" ("+año_publicacion+", "+duracion+", "+clasificacion)


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
    # print(contenido_x_director)

    elif int(inputs[0]) == 8:
        n= int(input("ingrese el numero n de top generos que quiere buscar"))
        print("Buscando ....")
    #    top_n_generos= controller.top_n_generos(n)
    # print(top_n_generos)

    elif int(inputs[0]) == 9:
        n= int(input("introduzca el n top de actores que desea consultar"))
        print("Buscando ....")
    #    top_n_actores= controller.top_n_actores(n)
    # print(top_n_actores)


    else:
        sys.exit(0)
sys.exit(0)