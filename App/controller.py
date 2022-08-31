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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def newController():
    """
    Crea una instancia del modelo
    """
    control = {
        'model': None
    }
    control['model'] = model.newCatalog()
    return control

# Funciones para la carga de datos
def loadData(control):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    ss_catalog = control['model']

    amazon_prime = loadTitles(ss_catalog, 'amazon_prime')
    disney_plus = loadTitles(ss_catalog, "disney_plus")
    hulu = loadTitles(ss_catalog, "hulu")
    netflix = loadTitles(ss_catalog, "netflix")
    
    return amazon_prime, disney_plus, hulu, netflix

def loadTitles(ss_catalog, ss_name):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    file_direc = "Challenge-1/"+ss_name+"_titles-utf8-small.csv"
    titlesfile = cf.data_dir + file_direc
    input_file = csv.DictReader(open(titlesfile, encoding='utf-8'))
    for title_inf in input_file:
        model.addTitle(ss_catalog, ss_name, title_inf)
    
    ss_name_catalog = ss_catalog[ss_name]
    return model.contentSize(ss_name_catalog), model.first_three_titles(ss_name_catalog), model.last_three_titles(ss_name_catalog)

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
