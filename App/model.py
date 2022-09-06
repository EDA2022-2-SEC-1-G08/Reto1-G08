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


import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import selectionsort as ss
from DISClib.Algorithms.Sorting import insertionsort as si
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
def addTitle(ss_catalog, ss_name, title_inf):
    pelicula = {}
    pelicula["title"] = title_inf["title"]
    pelicula["release_year"] = title_inf["release_year"]
    pelicula["rating"] = title_inf["rating"]
    pelicula["duration"] = title_inf["duration"]
    lt.addLast(ss_catalog[ss_name], pelicula)
    return ss_catalog

# Funciones para creacion de datos

# Funciones de consulta
# ss_name_catalog == ss_catalog[ss_name] = ss_catalog["amazon_prime" o "disney_plus" etc]

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
        elif movie1["duration"]<movie2["duration"]:
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
    end_time = getTime()
    deltaTime = float(end_time - start_time)
    return result, deltaTime

def getTime():
    return float(time.perf_counter()*1000)