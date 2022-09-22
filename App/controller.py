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
def newController(dataStructure):
    """
    Crea una instancia del modelo
    """
    control = {
        'model': None
    }
    control['model'] = model.newCatalog(dataStructure)
    return control

# Funciones para la carga de datos
def loadData(control, file, ordenar):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    ss_catalog = control['model']
    

    amazon_prime = loadTitles(ss_catalog, 'amazon_prime', file, "Amazon Prime", ordenar)
    disney_plus = loadTitles(ss_catalog, "disney_plus", file, "Disney Plus", ordenar)
    hulu = loadTitles(ss_catalog, "hulu", file, "Hulu", ordenar)
    netflix = loadTitles(ss_catalog, "netflix", file, "Netflix", ordenar)
    
    return amazon_prime, disney_plus, hulu, netflix

def loadTitles(ss_catalog, ss_name, file, empresa, ordenar):
    """
    Carga los contenidos del archivo.
    """
    file_direc = "Challenge-1/"+ss_name+file
    titlesfile = cf.data_dir + file_direc
    input_file = csv.DictReader(open(titlesfile, encoding='utf-8'))
    for title_inf in input_file:
        model.addTitle(ss_catalog, ss_name, title_inf, empresa, ordenar)
    
    ss_name_catalog = ss_catalog[ss_name]
    return model.contentSize(ss_name_catalog), model.first_three_titles(ss_name_catalog),model.last_three_titles(ss_name_catalog)

# Funciones de ordenamiento
def sortTitles(control, sort):
    return model.sortTitles(control["model"], sort)
# Funciones de consulta sobre el catálogo
def listar_peliculas_estrenadas_en_un_periodo(control, lim_inf, lim_sup):
    ss_catalog = control["model"]
    peliculas = model.listar_peliculas_estrenadas_en_un_periodo(ss_catalog, lim_inf, lim_sup)

    return model.contentSize(peliculas), model.first_three_titles(peliculas), model.last_three_titles(peliculas)

def listar_programas_agregados_en_un_periodo(control, fecha_inicial,fecha_final):
    ss_catalog = control["model"]
    programas = model.listar_programas_agregados_en_un_periodo(ss_catalog, fecha_inicial,fecha_final)
    return model.contentSize(programas), model.first_three_titles(programas), model.last_three_titles(programas)

def encontrar_contenido_x_actor(control, actor):
    ss_catalog = control["model"]
    programas_actor_x, n_peliculas, n_programas = model.encontrar_contenido_x_actor(ss_catalog, actor)
    return model.contentSize(programas_actor_x), n_peliculas, n_programas, model.first_three_titles(programas_actor_x), model.last_three_titles(programas_actor_x)

def encontrar_contenido_x_genero(control, genero):
    ss_catalog = control["model"]
    programas_genero_x, n_peliculas, n_programas = model.encontrar_contenido_x_genero(ss_catalog, genero)
    return model.contentSize(programas_genero_x), n_peliculas, n_programas, model.first_three_titles(programas_genero_x), model.last_three_titles(programas_genero_x)

def top_n_actores_con_mas_participaciones(control, top):
    ss_catalog = control["model"]
    actores = model.top_n_actores_con_mas_participaciones(ss_catalog, top)
    return actores

def contenido_x_pais(control, pais):
    ss_catalog = control["model"]
    contenido_producido_x_pais = model.contenido_producido_en_pais(ss_catalog, pais)
    return contenido_producido_x_pais

def top_n_generos(control, n):
    ss_catalog = control["model"]
    return model.top_n_generos(ss_catalog, n)
