# Programa inspirado en la agenda de contactos por consola

""" Crea un programa que permita gestionar una biblioteca personal. Las funcionalidades pueden incluir:
Agregar un libro: Permite al usuario agregar libros con información como título, autor, género y año de publicación.
Eliminar un libro: Elimina un libro de la biblioteca utilizando el título como clave.
Buscar un libro: Busca un libro por su título y muestra la información completa si existe.
Listar todos los libros: Muestra una lista de todos los libros almacenados en la biblioteca.
Salir del programa. """

def mostrar_menu():
    print("\nGestión de biblioteca:")
    print("1. Agregar un libro")
    print("2. Eliminar un libro")
    print("3. Buscar un libro")
    print("4. Listar todos los libros")
    print("5. Salir del programa")
    print("\n")

def agregar_libro(biblioteca):
    titulo = input("Por favor introduzca el nombre completo del libro: ")
    autor = input("Por favor introduzca el nombre del autor: ")
    genero = input("Por favor introduzca el género del libro: ")
    anio = input("Por favor introduzca el año de publicación del libro: ")
    biblioteca[titulo] = {"autor": autor, "genero": genero, "anio": anio}
    print(f"¡Se ha agregado el libro '{titulo}' exitosamente!")

def eliminar_libro(biblioteca):
    titulo = input("Ingrese el título del libro que desea eliminar: ")
    if titulo in biblioteca:
        del biblioteca[titulo]
        print(f"El libro '{titulo}' ha sido eliminado correctamente.")
    else:
        print(f"No se ha encontrado un libro con el título '{titulo}'.")

def buscar_libro(biblioteca):
    titulo = input("Ingrese el título del libro que está buscando: ")
    if titulo in biblioteca:
        print(f"Título: {titulo}")
        print(f"Autor: {biblioteca[titulo]['autor']}")
        print(f"Género: {biblioteca[titulo]['genero']}")
        print(f"Año: {biblioteca[titulo]['anio']}")
    else:
        print(f"El libro '{titulo}' no ha sido encontrado en la biblioteca.")

def listar_libros(biblioteca):
    if biblioteca:
        print("Lista de libros:")
        for titulo, info in biblioteca.items():
            print(f"Título: {titulo}")
            print(f"Autor: {info['autor']}")
            print(f"Género: {info['genero']}")
            print(f"Año: {info['anio']}")
            print("-" * 20)
    else:
        print("La biblioteca aún está vacía.")

def gestion_biblioteca():
    biblioteca = {}

    while True:
        mostrar_menu()
        opcion = input("Por favor elija una opción: ")
        print("\n")

        if opcion == "1":
            agregar_libro(biblioteca)
        elif opcion == "2":
            eliminar_libro(biblioteca)
        elif opcion == "3":
            buscar_libro(biblioteca)
        elif opcion == "4":
            listar_libros(biblioteca)
        elif opcion == "5":
            print("Saliendo de la biblioteca... ¡Hasta luego!")
            break
        else:
            print("Por favor seleccione una opción válida (del 1 al 5).")

gestion_biblioteca()
