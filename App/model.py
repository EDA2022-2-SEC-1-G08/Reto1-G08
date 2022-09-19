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


from datetime import datetime
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
    pelicula["descripcion"] = title_inf["description"]
    pelicula["empresa"] = empresa

    lt.addLast(ss_catalog[ss_name], pelicula)
    if ordenar[0] == "1":
        sm.sort(ss_catalog[ss_name], cmpContentByReleaseYear)

    return ss_catalog

# Funciones para creacion de datos
# Funciones de consulta
def listar_programas_agregados_en_un_periodo(catalog, fecha_inicial,fecha_final):
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
    return peliculas

def listar_peliculas_estrenadas_en_un_periodo(catalog, lim_inf, lim_sup):
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
    return peliculas

def contentSize(ss_name_catalog):
    return lt.size(ss_name_catalog)

def first_three_titles(ss_name_catalog):
    titles = lt.subList(ss_name_catalog, 1, 3)
    return titles

def last_three_titles(ss_name_catalog):
    titles = lt.subList(ss_name_catalog, lt.size(ss_name_catalog)-3, 3)
    return titles

# Funciones utilizadas para comparar elementos dentro de una lista
def comparecontents(content1, content):
    if content1.lower() == content['name'].lower():
        return 0
    elif content1.lower() > content1['name'].lower():
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