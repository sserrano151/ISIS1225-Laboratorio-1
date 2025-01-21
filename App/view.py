"""
 * Copyright 2024, Departamento de sistemas y Computación,
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
 * contribuciones:
 *
 * Dario Correal - Version inicial
 * Santiago Arteaga - Otras versiones
 * Andres Rodriguez - Última version
 """

import sys

import App.logic as logic

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion se hace 
la solicitud a la lógica para ejecutar la operación solicitada
"""

# Carpeta de datos
dataFolder = "GoodReads"


def new_logic():
    """
    Función que crea una nueva instancia de la lógica

    :return: Nueva instancia de la lógica
    :rtype: logic
    """
    app = logic.new_logic()
    return app


def print_menu():
    """
    Imprime el menú de opciones en consola para el usuario
    """
    print("Opciones:")
    print("1- Cargar Libros")
    print("2- Cargar Tags")
    # TODO: Mods Lab 1, agregar la opcion 3.
    # Agregue la opción 3 para cargar los tags de los libros.
    # Pueede guiarse de las opciones 1 y 2.
    print("0- Salir")


def load_books(app):
    """
    Función que carga los libros en la aplicación. 
    Carga los libros desde el archivo books-small.csv y los almacena en la aplicación

    :param app: Aplicación de la lógica
    :type app: logic
    """
    books = logic.load_books(app,
                             "GoodReads/books-small.csv")
    return books


def load_tags(app):
    """
    Función que carga los tags en la aplicación.
    Carga los tags desde el archivo tags.csv y los almacena en la aplicación

    :param app: Aplicación de la lógica
    :type app: logic
    """
    tags = logic.load_tags(app,
                           "GoodReads/tags.csv")
    return tags


def load_books_tags(app):
    """
    Función que carga los tags de los libros en la aplicación.
    Carga los tags de los libros desde el archivo book_tags-small.csv y los almacena en la aplicación

    :param app: Aplicación de la lógica
    :type app: logic
    """
    booksTags = logic.load_books_tags(app,
                                      "GoodReads/book_tags-small.csv")
    return booksTags


# Se crea la controlador asociado a la vista
app = new_logic()

# main del ejercicio


def main():
    """
    Función principal del programa.
    Presenta el menu de opciones y ejecuta las operaciones solicitadas por el usuario.
    """

    working = True
    # ciclo del menu
    while working:
        print_menu()
        inputs = input("Seleccione una opción para continuar\n")
        if int(inputs[0]) == 1:
            print("Cargando información de libros....")
            books = load_books(app)
            print("Total de libros cargados: " + str(books) + "\n")

        elif int(inputs[0]) == 2:
            print("Cargando información de tags....")
            tags = load_tags(app)
            print("Total de tags cargados: " + str(tags) + "\n")

        # TODO: Mods Lab 1, agregar la funcion opt 3 -> load_book_tags().
        # Agregue la opción 3 que llama a la función load_books_tags() (creada en la lógica).
        # Esta función carga los tags de los libros en el catalogo.
        # Puede guiarse de las opciones 1 y 2.
        # Imprima el total de tags de los libros cargados.
        elif int(inputs[0]) == 3:
            pass

        elif int(inputs[0]) == 0:
            working = False
            print("\nGracias por utilizar el programa.")

        else:
            print("Opcion erronea, vuelva a elegir.\n")
    sys.exit(0)
