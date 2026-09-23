"""Programa principal del catalogo de coleccionables."""

import catalog as catalog_module


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


def ask_price():
    """Pide el precio por teclado y lo devuelve como numero."""
    raw_price = input("Precio: ").strip()

    try:
        return float(raw_price)
    except ValueError:
        raise ValueError("El precio debe ser un numero.")


def option_add_piece(catalog):
    """Pide los datos de una pieza nueva y la agrega al catalogo."""
    print("")
    print("--- Agregar pieza ---")

    piece_id = input("ID: ").strip()
    name = input("Nombre: ").strip()
    category = input("Categoria: ").strip()

    try:
        price = ask_price()
        status = input("Estado (disponible, reservada, vendida): ").strip()
        description = input("Descripcion: ").strip()

        if catalog_module.piece_exists(catalog, piece_id):
            raise ValueError("Ya existe una pieza con el id '" + piece_id + "'.")

        piece = catalog_module.add_piece(
            piece_id, name, category, price, status, description
        )
        catalog.append(piece)
        print("Pieza agregada correctamente.")

    except ValueError as error:
        print("No se pudo agregar la pieza: " + str(error))


def print_piece(piece):
    """Muestra los datos de una pieza en una sola linea."""
    print(
        piece["id"]
        + " | "
        + piece["name"]
        + " | "
        + piece["category"]
        + " | "
        + str(piece["price"])
        + " | "
        + piece["status"]
    )


def option_list_pieces(catalog):
    """Muestra por pantalla todas las piezas guardadas."""
    print("")
    print("--- Piezas del catalogo ---")

    if len(catalog) == 0:
        print("Todavia no hay piezas guardadas.")
        return

    for piece in catalog:
        print_piece(piece)


def option_available_pieces(catalog):
    """Muestra solo las piezas que estan en estado disponible."""
    print("")
    print("--- Piezas disponibles ---")

    try:
        available = catalog_module.filter_by_status(catalog, "disponible")
    except ValueError as error:
        print("No se pudieron filtrar las piezas: " + str(error))
        return

    if len(available) == 0:
        print("No hay piezas disponibles ahora mismo.")
        return

    for piece in available:
        print_piece(piece)


def option_average_price(catalog):
    """Muestra el precio promedio de las piezas del catalogo."""
    print("")
    print("--- Precio promedio ---")

    average = catalog_module.get_average_price(catalog)

    if len(catalog) == 0:
        return

    print("El precio promedio es " + str(round(average, 2)) + " euros.")


def main():
    """Mantiene el menu en bucle hasta que el usuario decide salir."""
    catalog = []

    while True:
        show_menu()
        option = input("Elige una opcion: ").strip()

        if option == "7":
            print("Hasta luego.")
            break
        elif option == "1":
            option_add_piece(catalog)
        elif option == "2":
            option_list_pieces(catalog)
        elif option == "3":
            option_available_pieces(catalog)
        elif option == "4":
            option_average_price(catalog)
        elif option in ["5", "6"]:
            print("Opcion todavia no disponible.")
        else:
            print("Opcion no valida, elige un numero del 1 al 7.")


if __name__ == "__main__":
    main()
