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
from sre_parse import expand_template
from tokenize import tabsize
from unittest import result
from wsgiref import headers
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from tabulate import tabulate
assert cf
from datetime import date, datetime

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
    print("0- Cargar información en el catálogo")
    print("1- Listar las películas estrenadas en un periodo")
    print("2- Listar programas de televisión agregados en un periodo de tiempo")
    print("3- Encontrar contenido donde participa un actor")
    print("4- Encontrar contenido por un género especifico")
    print("5- Encontrar contenido producido en un país")
    print("6- Encontrar contenido con un director involucrado")
    print("7- Listar el TOP (N) de los géneros con más contenido")
    print("8- Listar el TOP (N) de los actores con más participaciones en contenido")
    print("9- Ordenar por fecha de lanzamiento")
    print("10- Elegír la estructura de datos")
    print("11- Salir")

def loadData(control, file, ordenar):
    """
    Solicita al controlador que cargue los datos en el modelo
    """
    amazon_prime, disney_plus, hulu, netflix = controller.loadData(control, file, ordenar)
    return amazon_prime, disney_plus, hulu, netflix

def dataStructure(dt:int):
    if dt == 1:
        tad = "SINGLE_LINKED"
    elif dt == 2:
        tad = "ARRAY_LIST"
    return tad

control = newController("ARRAY_LIST")
dt = 2


def printPeliculasRangoFechas(registros):
    n_registros, primeros, ultimos = registros
    info = {"Tipo": [], "Año": [], "Nombre": [], "Duración": [], "Servicio": [], "Director": [], "Actores": []}
    if lt.size(primeros):
        print("Número de películas encontrados que cumplen la condición: ", n_registros)
        print("Tabla de los primeros 3 y ultimos 3 registros encontrados entre las fechas indicadas")
        for registro in lt.iterator(primeros):
            info["Nombre"].append(registro["title"])
            info["Año"].append(registro["release_year"])
            info["Tipo"].append(registro["type"])
            info["Servicio"].append(registro["empresa"])
            info["Duración"].append(registro["duration"])
            info["Director"].append(registro["director"])
            info["Actores"].append(registro["cast"])
        for registro in lt.iterator(ultimos):
            info["Nombre"].append(registro["title"])
            info["Año"].append(registro["release_year"])
            info["Tipo"].append(registro["type"])
            info["Servicio"].append(registro["empresa"])
            info["Duración"].append(registro["duration"])
            info["Director"].append(registro["director"])
            info["Actores"].append(registro["cast"])
        titulos = ["Tipo", "Año", "Nombre", "Duración", "Plataforma", "Director", "Actores"]
        print(tabulate(info, headers=titulos, tablefmt="grid", maxcolwidths=30))
    else:
        print("No se encontraron registro en el rango de fechas indicado")
def printProgramasTVRangoFechas(programas):
    n_registros, primeros, ultimos = programas
    info = {"Tipo": [], "Nombre": [], "Fecha de Adición": [], "Duración": [], "Año": [], "Servicio": [], "Director": [], "Actores": []}
    if lt.size(primeros):
        print("Número de películas encontrados que cumplen la condición: ", n_registros)
        print("Tabla de los primeros 3 y ultimos 3 registros encontrados entre las fechas indicadas")
        for registro in lt.iterator(primeros):
            info["Nombre"].append(registro["title"])
            info["Fecha de Adición"].append(registro["fecha_adicion"])
            info["Año"].append(registro["release_year"])
            info["Tipo"].append(registro["type"])
            info["Servicio"].append(registro["empresa"])
            info["Duración"].append(registro["duration"])
            info["Director"].append(registro["director"])
            info["Actores"].append(registro["cast"])
        for registro in lt.iterator(ultimos):
            info["Nombre"].append(registro["title"])
            info["Fecha de Adición"].append(registro["fecha_adicion"])
            info["Año"].append(registro["release_year"])
            info["Tipo"].append(registro["type"])
            info["Servicio"].append(registro["empresa"])
            info["Duración"].append(registro["duration"])
            info["Director"].append(registro["director"])
            info["Actores"].append(registro["cast"])
        titulos = ["Tipo", "Nombre", "Fecha de Adición", "Duración", "Año", "Plataforma", "Director", "Actores"]
        print(tabulate(info, headers=titulos, tablefmt="grid", maxcolwidths=30))
    else:
        print("No se encontraron registro en el rango de fechas indicado")

def printContenidoPorGenero(contenido_genero):
    n_registros, n_peliculas, n_programas, primeros, ultimos = contenido_genero
    info = {
            "Nombre": [], 
            "Año": [],
            "Director": [],
            "Servicio": [],
            "Duración": [],
            "Actores": [],
            "País": [],
            "Genero": [],
            "Descripción": [] 
            }
    cantidad = {"Total": [n_registros], "N_Peliculas": [n_peliculas], "N_programas":[n_programas]}
    print(tabulate(cantidad, headers=["Total de Registros", "Numero de Películas", "Número de Programas de TV"], tablefmt="grid"))
    if lt.size(primeros):
        print("Número de películas encontrados que cumplen la condición: ", n_registros)
        print("Tabla de los primeros 3 y ultimos 3 registros encontrados entre las fechas indicadas")
        for registro in lt.iterator(primeros):
            info["Nombre"].append(registro["title"])
            info["Descripción"].append(registro["descripcion"])
            info["Año"].append(registro["release_year"])
            info["Servicio"].append(registro["empresa"])
            info["Duración"].append(registro["duration"])
            info["Director"].append(registro["director"])
            info["Actores"].append(registro["cast"])
            info["País"].append(registro["país"])
            info["Genero"].append(registro["genero"])
        for registro in lt.iterator(ultimos):
            info["Nombre"].append(registro["title"])
            info["Descripción"].append(registro["descripcion"])
            info["Año"].append(registro["release_year"])
            info["Servicio"].append(registro["empresa"])
            info["Duración"].append(registro["duration"])
            info["Director"].append(registro["director"])
            info["Actores"].append(registro["cast"])
            info["País"].append(registro["país"])
            info["Genero"].append(registro["genero"])
        titulos = ["Nombre", "Año", "Director", "Plataforma", "Duración", "Actores", "País", "Genero", "Descripción"]
        print(tabulate(info, headers=titulos, tablefmt="grid", maxcolwidths=20))
    else:
        print("No se encontraron registro en el rango de fechas indicado")

def printTopActoresMayorParticipaciones(actores, top):
    por_genero = {"Actor": [], "Participaciones": [], "MayorGenero": []}
    por_tipo = {"Actor": [], "Plataformas": []}
    compas = {"Actor": [], "Colaboraciones": []}
    
    print("El Top ", top, "Actores con más participaciones es...")
    for registro in lt.iterator(actores):
        plataforma = {"plataforma": [], "type":[], "veces": []}
        por_genero["Actor"].append(registro["nombre"])
        por_tipo["Actor"].append(registro["nombre"])
        compas["Actor"].append(registro["nombre"])
        otro = 2
        for plt in registro["n_participaciones_x_plataforma"]:
            if plt in plataforma["plataforma"]:
                plataforma["plataforma"].append(" ")
            elif otro:
                plataforma["plataforma"].append(plt)
                
            for type in registro["n_participaciones_x_plataforma"][plt]:
                plataforma["type"].append(type)
                plataforma["veces"].append((registro["n_participaciones_x_plataforma"][plt][type]))
        
        por_genero["Participaciones"].append(registro["n_participaciones"])
        generos = registro["n_generos"]
        mayor_genero = max(generos, key=generos.get)
        por_genero["MayorGenero"].append(mayor_genero)
        por_tipo["Plataformas"].append(tabulate(plataforma, tablefmt="plain"))
        compas["Colaboraciones"].append(", ".join(registro["actores"]))
    print(tabulate(plataforma))
    print(tabulate(por_genero, headers=["Actor", "Número de Participaciones", "Genero en el que más participó"], tablefmt="grid", maxcolwidths=30))
    print(tabulate(por_tipo, headers=["Actor", "Participaciones por plataforma"], tablefmt="grid", maxcolwidths=30, showindex=[x for x in range(1, int(top)+1)]))
    print(tabulate(compas, headers=["Actor", "Compañeros"], tablefmt="grid", maxcolwidths=30))

def printContenidoPorActor(contenido_actor):
    n_registros, n_peliculas, n_programas, primeros, ultimos = contenido_actor
    info = {
            "Nombre": [], 
            "Año": [],
            "Director": [],
            "Servicio": [],
            "Duración": [],
            "Actores": [],
            "País": [],
            "Genero": [],
            "Descripción": [] 
            }
    cantidad = {"Total": [n_registros], "N_Peliculas": [n_peliculas], "N_programas":[n_programas]}
    print(tabulate(cantidad, headers=["Total de Registros", "Numero de Películas", "Número de Programas de TV"], tablefmt="grid"))
    if lt.size(primeros):
        print("Número de películas encontrados que cumplen la condición: ", n_registros)
        print("Tabla de los primeros 3 y ultimos 3 registros encontrados entre las fechas indicadas")
        for registro in lt.iterator(primeros):
            info["Nombre"].append(registro["title"])
            info["Descripción"].append(registro["descripcion"])
            info["Año"].append(registro["release_year"])
            info["Servicio"].append(registro["empresa"])
            info["Duración"].append(registro["duration"])
            info["Director"].append(registro["director"])
            info["Actores"].append(registro["cast"])
            info["País"].append(registro["país"])
            info["Genero"].append(registro["genero"])
        for registro in lt.iterator(ultimos):
            info["Nombre"].append(registro["title"])
            info["Descripción"].append(registro["descripcion"])
            info["Año"].append(registro["release_year"])
            info["Servicio"].append(registro["empresa"])
            info["Duración"].append(registro["duration"])
            info["Director"].append(registro["director"])
            info["Actores"].append(registro["cast"])
            info["País"].append(registro["país"])
            info["Genero"].append(registro["genero"])
        titulos = ["Nombre", "Año", "Director", "Plataforma", "Duración", "Actores", "País", "Genero", "Descripción"]
        print(tabulate(info, headers=titulos, tablefmt="grid", maxcolwidths=20))
    else:
        print("No se encontraron registro en los que participe el actor indicado")

def printContenidoxPais(contenido_pais):
    deltatime, num_prog, num_pel, primeros_3_contenidos, ultimos_3_contenidos = contenido_pais

    #Imprimimos la tabla de la cantidad de contenido
    info_num = {"Programas": [num_prog], "Películas": [num_pel]}
    print(tabulate(info_num, headers=["Numero de Programas", "Numero de Películas"], tablefmt="grid"))

    info = {
            "Titulo": [], 
            "Fecha de lanzamiento": [],
            "Director": [],
            "Servicio": [],
            "Duración": [],
            "Actores": [],
            "País": [],
            "Genero": [],
            "Descripción": [] 
            }
    if lt.size(primeros_3_contenidos):
        print("Tabla de los primeros 3 y ultimos 3 contenidos del país dado")
        for registro in lt.iterator(primeros_3_contenidos):
            info["Titulo"].append(registro["title"])
            info["Fecha de lanzamiento"].append(registro["release_year"])
            info["Servicio"].append(registro["empresa"])
            info["Duración"].append(registro["duration"])
            info["Director"].append(registro["director"])
            info["Actores"].append(registro["cast"])
            info["País"].append(registro["país"])
            info["Genero"].append(registro["genero"])
            info["Descripción"].append(registro["descripcion"])
        for registro in lt.iterator(ultimos_3_contenidos):
            info["Titulo"].append(registro["title"])
            info["Descripción"].append(registro["descripcion"])
            info["Fecha de lanzamiento"].append(registro["release_year"])
            info["Servicio"].append(registro["empresa"])
            info["Duración"].append(registro["duration"])
            info["Director"].append(registro["director"])
            info["Actores"].append(registro["cast"])
            info["País"].append(registro["país"])
            info["Genero"].append(registro["genero"])
        titulos = ["Titulo", "Fecha de lanzamiento", "Director", "Plataforma", "Duración", "Actores", "País", "Genero", "Descripción"]
        print(tabulate(info, headers=titulos, tablefmt="grid", maxcolwidths=20))
    else:
        print("No se encontraron contenidos hechos en el país dado")
    
    print("El requerimiento se demoró", deltatime)

def printTopNGeneros(TopNGeneros):
    top_n_numbers, top_n_names, chopped_info_per_ss = TopNGeneros
    n = lt.size(top_n_names)

    
    print("TOP", n, "de los géneros con el mayor número de contenido")
    #Pintamos la tabla de conteos generales
    info_generos_counts = { "Generos": [top_n_names], "Conteo": [top_n_numbers]}
    print(tabulate(info_generos_counts, headers=["Generos", "Numero de Contenido"], tablefmt="grid"))

    #Hacemos la columna de los rankings
    col_num_rank = []
    i=1
    n = lt.size(top_n_names)
    while i<= n:
        col_num_rank.append(i)
        i+=1
    
    #Columna INDEX --> top_n_names
    #Columna count
    col_num_prog_pel_per_genre = []
    for nombre_generos in top_n_names:
        num_prog = 0
        num_pel = 0
        for s_streaming in chopped_info_per_ss:
            Generos_per_ss = chopped_info_per_ss[s_streaming]
            num_prog+= Generos_per_ss[nombre_generos][0]
            num_pel+= Generos_per_ss[nombre_generos][1]
        text = "Programas: "+str(num_prog)+"\n Peliculas: "+str(num_pel)
        col_num_prog_pel_per_genre.append(text)
    
    #Columna Streaming Services (A mostrar: El nombre de la plataforma, y su respectivo conteo de contenido [sin importar el tipo])
    # ---> Es claro que estamos haciendo el mismo recorrido que en el anterior loop, pero no lo unimos para mantener el código mucho más ordenado
    #      Ya que no afecta demasiado en el orden de crecimiento.
    col_num_per_streaming_service = []
    for nombre_generos in top_n_names:
        chopped_text = []
        for s_streaming in chopped_info_per_ss:
            Generos_per_ss = chopped_info_per_ss[s_streaming]
            num_cont_per_ss = Generos_per_ss[nombre_generos][0] + Generos_per_ss[nombre_generos][1]
            subtext = s_streaming+": "+str(num_cont_per_ss)
            chopped_text.append(subtext)
        joined_text = "\n".join(chopped_text)
        col_num_per_streaming_service.append(joined_text)
    
    columnas = {
        "Numeros ranking": col_num_rank,
        "Nombre_generos": top_n_names,
        "Count total": top_n_numbers,
        "Columna Count Peliculas y Programas": col_num_prog_pel_per_genre,
        "Columna Streaming Services": col_num_per_streaming_service
    }

    titulos = ["Rank", "Género", "Numero de Contenido", "Numero de Contenido según Tipo", "Servicios de Streaming"]
    print(tabulate(columnas, headers=titulos, tablefmt="grid", maxcolwidths=20))
    


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs) == 0:
        
        tad = dataStructure(dt)
        control = newController(tad)
        file = tamanoDeMuestra()
        sizeDatos = file[1]
        file = file[0]

        ordenar = 2
        print("¿Desea que los datos sean ordenados por fecha de lanzamiento?")
        print("1- Sí")
        print("2- No")
        ordenar = input()

        print("Cargando información de los archivos ....")
        print("Estructura de Datos Utilizada")
        print(control["model"]["hulu"]["type"])
        print()
        amazon_prime, disney_plus, hulu, netflix = loadData(control, file, ordenar)
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
        
    
    elif int(inputs) == 1:
        lim_inf= int(input("Introduzca el limite inferior para el que quiere buscar las peliculas: "))
        lim_sup= int(input("Introduzca el limite superior para el que quiere buscar las peliculas: "))
        print("Buscando ....")
        peliculas = controller.listar_peliculas_estrenadas_en_un_periodo(control, lim_inf, lim_sup)
        printPeliculasRangoFechas(peliculas)

    elif int(inputs) == 2:
        fecha_inicial= input("Introduzca la fecha inicial, con formato: %B %d, %Y : ")
        fecha_final= input("Introduzca la fecha final, con formato: %B %d, %Y : ")
        print("Buscando....")
        programas = controller.listar_programas_agregados_en_un_periodo(control, fecha_inicial,fecha_final)
        printProgramasTVRangoFechas(programas)

    elif int(inputs) == 3:
        nombre_actor= input("introduzca el nombre del autor que desea consultar: ")
        print("Buscando ....")
        contenido_actor= controller.encontrar_contenido_x_actor(control, nombre_actor)
        printContenidoPorActor(contenido_actor)

    elif int(inputs) == 4:
        genero= input("introduzca el genero que desea buscar: ")
        print("Buscando ....")
        contenido_genero= controller.encontrar_contenido_x_genero(control, genero)
        printContenidoPorGenero(contenido_genero)

    elif int(inputs) == 5:
        pais= input("introduzca el pais a consultar: ")
        print("Buscando ....")
        contenido_pais = controller.contenido_x_pais(control, pais)
        printContenidoxPais(contenido_pais)

    elif int(inputs) == 6:
        director= input("introduzca el director a consultar")
        print("Buscando ....")
    #    contenido_x_director= controller.contenido_x_director(director)
    # print(contenido_x_director)1

    elif int(inputs) == 7:
        n= int(input("ingrese el numero n de top generos que quiere buscar: "))
        print("Buscando ....")
        top_n_generos= controller.top_n_generos(control, n)
        printTopNGeneros(top_n_generos)

    elif int(inputs) == 8:
        top= int(input("Introduzca el N top de actores que desea consultar "))
        print("Buscando ....")
        actores = controller.top_n_actores_con_mas_participaciones(control, top)
        printTopActoresMayorParticipaciones(actores, top)

    elif int(inputs) == 9:
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

    elif int(inputs) == 11:
        sys.exit(0)

    else:
        print("Por favor seleccione una opción válida")
        continue
sys.exit(0)