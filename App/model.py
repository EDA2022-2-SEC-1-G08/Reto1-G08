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
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    ss_catalog = {'amazon_prime': None,
               'disney_plus': None,
               'hulu': None,
               'netflix': None}

    ss_catalog['amazon_prime'] = lt.newList('SINGLE_LINKED')
    ss_catalog['disney_plus'] = lt.newList('SINGLE_LINKED')
    ss_catalog['hulu'] =lt.newList('SINGLE_LINKED')
    ss_catalog['netflix'] = lt.newList('SINGLE_LINKED')

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

# Funciones de ordenamiento