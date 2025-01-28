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
 * Santiago Arteaga - Otras versiones
 * Andres Rodriguez - Última version
 """

import os


# Importar el modulo de la estructura de datos set
from DataStructures import set as set

# Directorio de datos de los archivos
data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

"""
La lógica se encarga de procesar los datos y realizar las operaciones
sobre ellos. En este caso, se encarga de cargar los datos y realizar
las consultas sobre ellos.
"""


def new_logic():
    """
    Inicializa los datos y crea un catalogo vacio. 

    Para esta actividad, un catalogo es un diccionario donde se guardan
    las estructuras de datos que representan los libros, los autores, los
    generos y la asociación entre libros y generos. 

    Se crea un catalogo con las siguientes atributos:
    - books: Set para guardar los libros.
    - tags: Set para guardar los generos.
    - book_tags: Set para guardar la asociación entre libros y generos.

    :return: Catalogo inicializado
    :rtype: dict
    """

    # Creación del catalogo vacio
    catalog = {
        "books": None,
        "tags": None,
        "book_tags": None,
    }

    # Inicialización de las estructuras de datos
    catalog["books"] = set.new_set()
    catalog["tags"] = set.new_set()
    catalog["book_tags"] = set.new_set()

    return catalog


# Funciones para la carga de datos

def load_books(catalog, filename):
    """
    Función que carga los libros en el catalogo.

    Por cada libro se toman sus autores y por cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.

    :param catalog: Catalogo de la aplicación
    :type catalog: dict
    :param filename: Nombre del archivo csv con los libros
    :type filename: str

    :returns: Tamaño del conjunto de libros
    :rtype: int
    """
    books = catalog["books"]
    booksfile = os.path.join(data_dir, filename)
    catalog["books"] = set.load_set(books, booksfile)
    if empty_books(catalog):
        return 0
    else:
        return book_size(catalog)


def load_tags(catalog, filename):
    """
    Carga todos los tags del archivo y los agrega a la lista de tags

    :param catalog: Catalogo de la aplicación
    :type catalog: dict
    :param filename: Nombre del archivo csv con los tags
    :type filename: str

    :returns: Tamaño del conjunto de tags
    :rtype: int
    """
    tags = catalog["tags"]
    tagsfile = os.path.join(data_dir, filename)
    catalog["tags"] = set.load_set(tags, tagsfile)

    if set.is_empty(tags):
        return 0
    else:
        return set.size(tags)


def load_books_tags(catalog, filename):
    """
    Carga los tags de los libros del archivo y los agrega a la lista
    de tags. Siga el mismo procedimiento que en la carga de libros.

    :param catalog: Catalogo de la aplicación
    :type catalog: dict
    :param filename: Nombre del archivo csv con los tags de los libros
    :type filename: str

    :returns: Tamaño del conjunto de tags de los libros
    :rtype: int
    """
    # TODO: Mods Lab 1, integrar vista y logica
    # Implemente una función que cargue los tags de los libros en el catalogo.
    # La función debe recibir el catalogo y el nombre del archivo csv con los tags de los libros.
    # La función debe cargar los tags de los libros del archivo y los agregar al conjunto book_tags del catalogo.
    # La función debe retornar el tamaño del conjunto de tags de los libros.
   
    def load_books_tags(catalog, filename):
    
    book_tags = catalog.get("Book_tags")
    book_tags_file = os.path.join(data_dir, filename)
    catalog["Book_tags"] = set.load_set(book_tags, book_tags_file)

    if book_tags is None:
        return None
    else:
        return set.size(catalog.get("Book_tags"))


# Funciones de consulta


def book_size(catalog):
    """
    Obtiene el tamaño del conjunto de libros.

    :param catalog: Catalogo de la aplicación
    :type catalog: dict

    :returns: Tamaño del conjunto de libros
    :rtype: int
    """
    return set.size(catalog["books"])


def tag_size(catalog):
    """
    Obtiene el tamaño del conjunto de tags.

    :param catalog: Catalogo de la aplicación
    :type catalog: dict

    :returns: Tamaño del conjunto de tags
    :rtype: int
    """
    return set.size(catalog["tags"])


def book_tag_size(catalog):
    """
    Obtiene el tamaño del conjunto de tags de los libros.

    :param catalog: Catalogo de la aplicación
    :type catalog: dict

    :returns: Tamaño del conjunto de tags de los libros
    :rtype: int
    """
    return set.size(catalog["book_tags"])


def empty_books(catalog):
    """
    Verifica si el conjunto de libros esta vacio.

    :param catalog: Catalogo de la aplicación
    :type catalog: dict

    :returns: True si el conjunto de libros esta vacio, False de lo contrario
    :rtype: bool
    """
    books = catalog["books"]
    return set.is_empty(books)


def empty_tags(catalog):
    """
    Verifica si el conjunto de tags esta vacio.

    :param catalog: Catalogo de la aplicación
    :type catalog: dict

    :returns: True si el conjunto de tags esta vacio, False de lo contrario
    :rtype: bool
    """
    tags = catalog["tags"]
    return set.is_empty(tags)


def empty_book_tags(catalog):
    """
    Verifica si el conjunto de tags de los libros esta vacio.

    :param catalog: Catalogo de la aplicación
    :type catalog: dict

    :returns: True si el conjunto de tags de los libros esta vacio, False de lo contrario
    :rtype: bool
    """
    book_tags = catalog["book_tags"]
    return set.is_empty(book_tags)
