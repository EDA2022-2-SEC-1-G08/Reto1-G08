"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from datetime import datetime, timedelta
from turtle import title
import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import selectionsort as ss
from DISClib.Algorithms.Sorting import insertionsort as si
from DISClib.Algorithms.Sorting import mergesort as sm
from DISClib.Algorithms.Sorting import quicksort as sq
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(dataStructure):
    ss_catalog = {'amazon_prime': None,
               'disney_plus': None,
               'hulu': None,
               'netflix': None}

    ss_catalog['amazon_prime'] = lt.newList(dataStructure)
    ss_catalog['disney_plus'] = lt.newList(dataStructure)
    ss_catalog['hulu'] =lt.newList(dataStructure)
    ss_catalog['netflix'] = lt.newList(dataStructure)

    return ss_catalog

# Funciones para agregar informacion al catalogo
def addTitle(ss_catalog, ss_name, title_inf, empresa, ordenar):
    pelicula = {}
    pelicula["id"] = title_inf["show_id"]
    pelicula["type"] = title_inf["type"]
    pelicula["title"] = title_inf["title"]
    pelicula["director"] = title_inf["director"]
    pelicula["cast"] = title_inf["cast"]
    pelicula["país"] = title_inf["country"]
    pelicula["fecha_adicion"] = title_inf["date_added"]
    pelicula["release_year"] = title_inf["release_year"]
    pelicula["rating"] = title_inf["rating"]
    pelicula["duration"] = title_inf["duration"]
    pelicula["genero"] = title_inf["listed_in"]
    pelicula["descripcion"] = title_inf["description"]
    pelicula["empresa"] = empresa

    lt.addLast(ss_catalog[ss_name], pelicula)
    if ordenar[0] == "1":
        sm.sort(ss_catalog[ss_name], cmpContentByReleaseYear)

    return ss_catalog

def addActor(ss_catalog, nombre, director, type, actores, generos, empresa, existente):
    if not existente:
        actor = {}
        actor["nombre"] = nombre
        actor["directores"] = []
        actor["n_participaciones"] = 1
        actor["n_participaciones_x_plataforma"] = {empresa : {type: 1},}
        actor["actores"] = []
        actor["n_generos"] = {}
        for compa in actores:
            if compa != "":
                actor["actores"].append(compa)
        for genero in generos:
            actor["n_generos"][genero] = 1
        lt.addLast(ss_catalog, actor)
        if director != "":
            actor["directores"].append(director)
    else:
        for registro in lt.iterator(ss_catalog):
            if registro["nombre"] == nombre:
                registro["n_participaciones"] += 1
                if not(director in registro["directores"]) and director != "":
                    registro["directores"].append(director)
                for compa in actores:
                    if not(compa in actores) and compa != "":
                        actor["actores"].append(compa)
                for genero in generos:
                    if genero in registro["n_generos"]:
                        registro["n_generos"][genero] += 1
                    else:
                        registro["n_generos"][genero] = 1
                
                if empresa in registro["n_participaciones_x_plataforma"]:
                    if type in registro["n_participaciones_x_plataforma"][empresa]:
                        if type != "":
                            registro["n_participaciones_x_plataforma"][empresa][type] += 1
                    else:
                        if type != "":
                            registro["n_participaciones_x_plataforma"][empresa][type] = 1
                else:
                    registro["n_participaciones_x_plataforma"][empresa] = {}
                    registro["n_participaciones_x_plataforma"][empresa][type] = 1
    return ss_catalog
# 

# Funciones para creacion de datos
# Funciones de consulta
def top_n_actores_con_mas_participaciones(catalog, top):
    amazon = catalog["amazon_prime"]
    disney = catalog["disney_plus"]
    hulu = catalog["hulu"]
    netflix = catalog["netflix"]
    empresas = [amazon, disney, hulu, netflix]
    actores = lt.newList("ARRAY_LIST")
    cont_movies = 0
    cont_TV = 0
    aux_actores = []
    
    for servicio in empresas:
        for i in range(contentSize(servicio)):
            registro = lt.getElement(servicio, i)
            cast = registro["cast"].split(", ")
            director = registro["director"]
            type = registro["type"]
            generos = registro["genero"].split(sep=", ")
            empresa = registro["empresa"]
            for actor in cast:
                if actor in aux_actores:
                    existente = True
                else:
                    existente = False
                    aux_actores.append(actor)
                if actor != "":
                    addActor(actores, actor, director, type, cast, generos, empresa, existente)
    sm.sort(actores, cmpActores)
    actores = lt.subList(actores, 0, 20)
    for i in lt.iterator(actores):
        print(i["nombre"],i["directores"])
    #print(aux_actores)

    #sm.sort(actores, cmpContentByTitle)
    return get_top_n_actores(actores, top)

def encontrar_contenido_x_genero(catalog, genero):
    times = getTime()
    amazon = catalog["amazon_prime"]
    disney = catalog["disney_plus"]
    hulu = catalog["hulu"]
    netflix = catalog["netflix"]
    empresas = [amazon, disney, hulu, netflix]
    contenido = lt.newList()
    cont_movies = 0
    cont_TV = 0
    for servicio in empresas:
        for i in range(contentSize(servicio)):
            registro = lt.getElement(servicio, i)
            type = registro["type"]
            generos = registro["genero"]
            generos = generos.split(sep=", ")
            if type == "TV Show":
                if genero in generos:
                    lt.addLast(contenido, registro)
                    cont_TV += 1
            elif type == "Movie":
                if genero in generos:
                    lt.addLast(contenido, registro)
                    cont_movies += 1

    sm.sort(contenido, cmpContentByTitle)
    timef = getTime()
    print(deltaTime(times, timef))
    return contenido, cont_movies, cont_TV

def encontrar_contenido_x_actor(catalog, actor):
    amazon = catalog["amazon_prime"]
    disney = catalog["disney_plus"]
    hulu = catalog["hulu"]
    netflix = catalog["netflix"]
    empresas = [amazon, disney, hulu, netflix]
    contenido = lt.newList()
    cont_movies = 0
    cont_TV = 0
    for servicio in empresas:
        for i in range(contentSize(servicio)):
            registro = lt.getElement(servicio, i)
            type = registro["type"]
            actores = registro["cast"]
            actores = actores.split(sep=", ")
            if type == "TV Show":
                if actor in actores:
                    lt.addLast(contenido, registro)
                    cont_TV += 1
            elif type == "Movie":
                if actor in actores:
                    lt.addLast(contenido, registro)
                    cont_movies += 1

    sm.sort(contenido, cmpContentByTitle)
    return contenido, cont_movies, cont_TV

def listar_programas_agregados_en_un_periodo(catalog, fecha_inicial,fecha_final):
    times = getTime()
    amazon = catalog["amazon_prime"]
    disney = catalog["disney_plus"]
    hulu = catalog["hulu"]
    netflix = catalog["netflix"]
    empresas = [amazon, disney, hulu, netflix]
    peliculas = lt.newList()
    fecha_inicial = datetime.strptime(fecha_inicial, "%B %d, %Y")
    fecha_final = datetime.strptime(fecha_final, "%B %d, %Y") 
    for servicio in empresas:
        for i in range(contentSize(servicio)):
            registro = lt.getElement(servicio, i)
            type = registro["type"]
            if type == "TV Show":
                fecha = registro["fecha_adicion"]
                if fecha != "":
                    fecha = datetime.strptime(fecha, "%Y-%m-%d")
                    if fecha >= fecha_inicial and fecha <= fecha_final:
                        lt.addLast(peliculas, registro)
    sm.sort(peliculas, cmpProgramsByDateAdded)
    timef = getTime()
    print(deltaTime(times, timef))
    return peliculas

def listar_peliculas_estrenadas_en_un_periodo(catalog, lim_inf, lim_sup):
    times = getTime()
    amazon = catalog["amazon_prime"]
    disney = catalog["disney_plus"]
    hulu = catalog["hulu"]
    netflix = catalog["netflix"]
    empresas = [amazon, disney, hulu, netflix]
    peliculas = lt.newList()
    for servicio in empresas:
        for i in range(contentSize(servicio)):
            registro = lt.getElement(servicio, i)
            type = registro["type"]
            if type == "Movie":
                year = int(registro["release_year"])
                if year >= lim_inf and year <= lim_sup:
                    lt.addLast(peliculas, registro)
    sm.sort(peliculas, cmpMoviesByReleaseYear)
    timef = getTime()
    print(deltaTime(times, timef))
    return peliculas

def contentSize(ss_name_catalog):
    return lt.size(ss_name_catalog)

def get_top_n_actores(catalog, top):
    actores = lt.subList(catalog, 2, int(top))
    return actores

def first_three_titles(ss_name_catalog):
    if lt.size(ss_name_catalog) < 3:
        titles = lt.subList(ss_name_catalog, 1, lt.size(ss_name_catalog))
    else:    
        titles = lt.subList(ss_name_catalog, 1, 3)
    return titles

def last_three_titles(ss_name_catalog):
    size = lt.size(ss_name_catalog)
    if size < 3:
        titles = lt.subList(ss_name_catalog, 1, size)
        
    else:    
        titles = lt.subList(ss_name_catalog, size-3, 3)
        
    return titles

def contenido_producido_en_pais(catalog, pais):
    amazon = catalog["amazon_prime"]
    disney = catalog["disney_plus"]
    hulu = catalog["hulu"]
    netflix = catalog["netflix"]
    empresas = [amazon, disney, hulu, netflix]

    #Ya que la lista está ordenada, podría solo cogerse los primeros 3 contenidos y los últimos 3 contenidos de cada servicio de streaming y hacer
    #sort a todo eso y, del orden resultante, sacar los primeros 3 y los ultimos 3.

    cont_prod_pais_every_serv = lt.newList("ARRAY_LIST") #Creamos la lista que tendrá todos los contenidos del país dado
    num_prog = 0
    num_pel = 0
    start_time = getTime()
    #Se rellena la lista
    for servicios in empresas:
        for contenido in lt.iterator(servicios):
            if contenido["país"] == pais:
                #Se agrega a la sublista mencionada el contenido si es del país
                lt.addLast(cont_prod_pais_every_serv, contenido)
                #Se cuentan los programas y las peliculas:
                if contenido["type"] == "TV Show":
                    num_prog+=1
                else:
                    num_pel+=1

    #Se ordena la lista
    sm.sort(cont_prod_pais_every_serv, cmpContentByTitle)
    
    primeros_3_contenidos = first_three_titles(cont_prod_pais_every_serv)
    ultimos_3_contenidos = last_three_titles(cont_prod_pais_every_serv)
    end_time = getTime()
    deltatime = deltaTime(start_time, end_time)

    return deltatime, num_prog, num_pel, primeros_3_contenidos, ultimos_3_contenidos

def  top_n_generos(catalog, n):

    #1. CREAMOS UNA ESTRUCTURA DE ALMACENAMIENTO CON LA INFORMACION DE TODOS LOS GENEROS ENCONTRADOS:

    generos_info = {} #Diccionario General
    chopped_info_per_ss = {}
    for nombre_servicios in catalog:
        generos_info_ss = {} #Subdiccionario con la información de una plataforma en específico. 
        #Estructura = {Nombre genero (str): [Numero de programas de dicho género (int), Numero de películas de dicho género(int), ...]
        for contenido in lt.iterator(catalog[nombre_servicios]):
            generos_contenido = contenido["genero"].split(", ")
            type = 1 #Type = 1 --> Pelicula, Type = 0 --> Programa
            if contenido["type"] == "TV Show":
                type = 0
            for genero in generos_contenido:
                if generos_info_ss.get(genero, 0) == 0:
                    generos_info_ss[genero] = [0, 0]
                generos_info_ss[genero][type] = generos_info_ss[genero][type]+1 #Actualizamos la información del subdiccionario
                generos_info[genero] = generos_info.get(genero, 0)+1 #Actualizamos la información del diccionario general
            
        chopped_info_per_ss[nombre_servicios] = generos_info_ss #Guardamos la info recolectada de cada uno de los servicios de streaming
    
    #2. BUSCAMOS LOS NOMBRES DE LOS GENEROS EN EL TOP N
    General_dict_values = lt.newList("ARRAY_LIST") #Creamos una lista que tendrá los valores de todas las llaves del diccionario general
    for nombre_genero in generos_info:
        lt.addLast(General_dict_values, generos_info[nombre_genero]) #Llenamos la lista
    sm.sort(General_dict_values, cmpRankingN) #Ordenamos la lista de mayor a menor (No funciona la funcion cmp)
    print(General_dict_values) 
    top_n_numbers = lt.subList(General_dict_values, 1, n) #Creamos una lista con los N mayores contenidos

    i = 1
    top_n_names = lt.newList("ARRAY_LIST") #Ya que solo tenemos los valores, toca ahora matchear esos numeros con las llaves. 
                                        #Este diccionario contendrá los nombres de las llaves.
    while i<=n:
        for nombre_genero in generos_info:
            if generos_info[nombre_genero] == lt.getElement(top_n_numbers, i): # - Si coincide el numero con el valor de la llave
                if i==1:                                        
                    lt.addLast(top_n_names, nombre_genero) 
                    break
                elif lt.getElement(top_n_numbers, i-1) == nombre_genero: # -- Si resulta que hay numeros repetidos
                    pass                                                 # -- Nos aseguramos de que no se guarde el mismo nombre
                else:
                    lt.addLast(top_n_names, nombre_genero)                      # - Agregamos el nombre a top_n_names
                    break
        i+=1
    
    #Con los diccionarios y los nombres a buscar, solo queda que en la vista se decida mostrar los que son.
    return top_n_numbers, top_n_names, chopped_info_per_ss


# Funciones utilizadas para comparar elementos dentro de una lista
def cmpActores(actor1, actor2):
    if actor1["n_participaciones"] > actor2["n_participaciones"]:
        return True
    elif actor1["n_participaciones"] == actor2["n_participaciones"]:
        if actor1["nombre"] < actor2["nombre"]:
            return True
        else:
            return False
    else:
        return False

def comparecontents(content1, content):
    if content1.lower() == content['name'].lower():
        return 0
    elif content1.lower() > content1['name'].lower():
        return 1
    return -1

def cmpRankingN(num1, num2):
    if num1 == num2:
        return 0
    elif num1 > num2:
        return 1
    return -1

# Funciones de comparación


def cmpContentByTitle(content1, content2):
    """
    Devuelve verdadero (True) si el title de movie1 es menor que los
    de movie2, en caso de que sean iguales tenga en cuenta el año de lanzamiento y en caso de que
    ambos criterios sean iguales tenga en cuenta el nombre del director, de lo contrario devuelva
    falso (False).
    Args:
    movie1: informacion de la primera pelicula que incluye sus valores 'title', ‘release_year’ y ‘director’
    movie2: informacion de la segunda pelicula que incluye su valor 'title', ‘release_year’ y ‘director’
    """
    if content1["title"] < content2["title"]:
        return True
    elif content1["title"] == content2["title"]:
        if content1["release_year"] < content2["release_year"]:
            return True
        elif content1["release_year"] == content2["release_year"]:
            if content1["duration"]<content2["duration"]:
                return True
            else:
                return False
        else:
            return False
    else:
        return False



def cmpProgramsByDateAdded(movie1, movie2):
    """
    Devuelve verdadero (True) si el date_added de movie1 es mayor que los
    de movie2, en caso de que sean iguales tenga en cuenta el titulo y en caso de que
    ambos criterios sean iguales tenga en cuenta la duración, de lo contrario devuelva
    falso (False).
    Args:
    movie1: informacion de la primera pelicula que incluye sus valores 'date_added', ‘title’ y ‘duration’
    movie2: informacion de la segunda pelicula que incluye su valor 'date_added', ‘title’ y ‘duration’
    """
    fecha1 = movie1["fecha_adicion"]
    fecha1 = datetime.strptime(fecha1, "%Y-%m-%d")
    fecha2 = movie2["fecha_adicion"]
    fecha2 = datetime.strptime(fecha2, "%Y-%m-%d")

    if fecha1 > fecha2:
        return True
    elif fecha1 == fecha2:
        if movie1["title"] > movie2["title"]:
            return True
        elif movie1["title"] == movie2["title"]:
            if movie1["duration"] > movie2["duration"]:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def cmpMoviesByReleaseYear(movie1, movie2):
    """
    Devuelve verdadero (True) si el release_year de movie1 son menores que los
    de movie2, en caso de que sean iguales tenga en cuenta el titulo y en caso de que
    ambos criterios sean iguales tenga en cuenta la duración, de lo contrario devuelva
    falso (False).
    Args:
    movie1: informacion de la primera pelicula que incluye sus valores 'release_year', ‘title’ y ‘duration’
    movie2: informacion de la segunda pelicula que incluye su valor 'release_year', ‘title’ y ‘duration’
    """
    if movie1["release_year"] < movie2["release_year"]:
        return True
    elif movie1["release_year"] == movie2["release_year"]:
        if movie1["title"] < movie2["title"]:
            return True
        elif movie1["title"] == movie2["title"]:
            if movie1["duration"]<movie2["duration"]:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
        
def cmpContentByReleaseYear(movie1, movie2):
    """
    Devuelve verdadero (True) si el release_year de movie1 son menores que los
    de movie2, en caso de que sean iguales tenga en cuenta el titulo, de lo contrario devuelva
    falso (False).
    Args:
    movie1: informacion de la primera pelicula que incluye sus valores 'release_year' y ‘title’
    movie2: informacion de la segunda pelicula que incluye su valor 'release_year' y ‘title’
    """
    if movie1["release_year"] < movie2["release_year"]:
        return True
    elif movie1["release_year"] == movie2["release_year"]:
        if movie1["title"] < movie2["title"]:
            return True
        else:
            return False
    else:
        return False
# Funciones de ordenamiento
def sortTitles(catalog, sort):
    times = []
    start_time = getTime()
    if int(sort) == 1:
        result = ss.sort(catalog["amazon_prime"],cmpMoviesByReleaseYear)
        result = ss.sort(catalog["disney_plus"],cmpMoviesByReleaseYear)
        result = ss.sort(catalog["hulu"],cmpMoviesByReleaseYear)
        result = ss.sort(catalog["netflix"],cmpMoviesByReleaseYear)
    elif int(sort) == 2:
        result = si.sort(catalog["amazon_prime"],cmpMoviesByReleaseYear)
        result = si.sort(catalog["disney_plus"],cmpMoviesByReleaseYear)
        result = si.sort(catalog["hulu"],cmpMoviesByReleaseYear)
        result = si.sort(catalog["netflix"],cmpMoviesByReleaseYear)
    elif int(sort) == 3:
        result = sa.sort(catalog["amazon_prime"],cmpMoviesByReleaseYear)
        result = sa.sort(catalog["disney_plus"],cmpMoviesByReleaseYear)
        result = sa.sort(catalog["hulu"],cmpMoviesByReleaseYear)
        result = sa.sort(catalog["netflix"],cmpMoviesByReleaseYear)
    elif int(sort) == 4:
        result = sq.sort(catalog["amazon_prime"],cmpMoviesByReleaseYear)
        result = sq.sort(catalog["disney_plus"],cmpMoviesByReleaseYear)
        result = sq.sort(catalog["hulu"],cmpMoviesByReleaseYear)
        result = sq.sort(catalog["netflix"],cmpMoviesByReleaseYear)
    elif int(sort) == 5:
        result = sm.sort(catalog["amazon_prime"],cmpMoviesByReleaseYear)
        result = sm.sort(catalog["disney_plus"],cmpMoviesByReleaseYear)
        result = sm.sort(catalog["hulu"],cmpMoviesByReleaseYear)
        result = sm.sort(catalog["netflix"],cmpMoviesByReleaseYear)
    end_time = getTime()
    deltaTime = float(end_time - start_time)
    return result, deltaTime

def getTime():
    return float(time.perf_counter()*1000)
def deltaTime(star, end):
    elapsed = float(end - star)
    return elapsed