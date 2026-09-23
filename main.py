"""Programa principal del catalogo de coleccionables."""


def show_menu():
    """Muestra las opciones disponibles del programa."""
    print("")
    print("=== Catalogo de coleccionables ===")
    print("1. Agregar pieza")
    print("2. Mostrar todas las piezas")
    print("3. Mostrar piezas disponibles")
    print("4. Ver precio promedio")
    print("5. Buscar pieza por ID")
    print("6. Eliminar pieza")
    print("7. Salir")


def main():
    """Mantiene el menu en bucle hasta que el usuario decide salir."""
    catalog = []

    while True:
        show_menu()
        option = input("Elige una opcion: ").strip()

        if option == "7":
            print("Hasta luego.")
            break
        elif option in ["1", "2", "3", "4", "5", "6"]:
            print("Opcion todavia no disponible.")
        else:
            print("Opcion no valida, elige un numero del 1 al 7.")


if __name__ == "__main__":
    main()
