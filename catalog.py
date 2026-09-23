"""Funciones del catalogo de piezas coleccionables.

Aqui van: agregar, listar, buscar, quitar, filtrar y las metricas.
Las validaciones se delegan siempre en el modulo validations.
"""

import validations


def add_piece(piece_id, name, category, price, status, description):
    """Valida los datos recibidos y devuelve la pieza como diccionario."""
    validations.validate_not_empty(piece_id, "id")
    validations.validate_not_empty(name, "name")
    validations.validate_not_empty(category, "category")
    validations.validate_not_empty(status, "status")
    validations.validate_not_empty(description, "description")

    validations.validate_price(price)
    validations.validate_status(status)
    validations.validate_description(description)

    piece = {
        "id": str(piece_id).strip(),
        "name": str(name).strip(),
        "category": str(category).strip(),
        "price": float(price),
        "status": status.strip().lower(),
        "description": str(description).strip(),
    }

    return piece


def list_pieces(catalog):
    """Devuelve una lista con los nombres de todas las piezas del catalogo."""
    if not isinstance(catalog, list):
        raise ValueError("El catalogo debe ser una lista.")

    names = []

    for piece in catalog:
        names.append(piece["name"])

    return names


def find_piece_by_id(catalog, piece_id):
    """Busca una pieza por su id y la devuelve, o None si no esta."""
    if not isinstance(catalog, list):
        raise ValueError("El catalogo debe ser una lista.")

    for piece in catalog:
        if piece["id"] == str(piece_id).strip():
            return piece

    return None


def remove_piece(catalog, piece_id):
    """Quita una pieza del catalogo por su id.

    Devuelve True si se pudo quitar y False si la pieza no estaba.
    """
    if not isinstance(catalog, list):
        raise ValueError("El catalogo debe ser una lista.")

    try:
        piece = find_piece_by_id(catalog, piece_id)

        if piece is None:
            raise ValueError("La pieza con id '" + str(piece_id) + "' no fue encontrada.")

        catalog.remove(piece)
        return True

    except ValueError as error:
        print("Error al quitar la pieza: " + str(error))
        return False


def piece_exists(catalog, piece_id):
    """Indica si una pieza esta en el catalogo, sin lanzar errores."""
    if not isinstance(catalog, list):
        raise ValueError("El catalogo debe ser una lista.")

    return find_piece_by_id(catalog, piece_id) is not None


def get_catalog_summary(catalog):
    """Cuenta cuantas piezas hay por cada categoria.

    Devuelve un diccionario donde la clave es la categoria y el valor
    es la cantidad de piezas de esa categoria.
    """
    if not isinstance(catalog, list):
        raise ValueError("El catalogo debe ser una lista.")

    summary = {}

    for piece in catalog:
        category = piece["category"]

        if category in summary:
            summary[category] = summary[category] + 1
        else:
            summary[category] = 1

    return summary


def get_pieces_by_category(catalog, category):
    """Devuelve los nombres de las piezas que pertenecen a una categoria.

    Si no hay coincidencias devuelve una lista vacia.
    """
    if not isinstance(catalog, list):
        raise ValueError("El catalogo debe ser una lista.")

    wanted = str(category).strip().lower()
    names = []

    for piece in catalog:
        if piece["category"].strip().lower() == wanted:
            names.append(piece["name"])

    return names


def filter_by_status(catalog, status):
    """Devuelve las piezas que tienen el estado indicado.

    Lanza ValueError si el estado no es uno de los permitidos.
    """
    if not isinstance(catalog, list):
        raise ValueError("El catalogo debe ser una lista.")

    validations.validate_status(status)

    wanted = status.strip().lower()
    found = []

    for piece in catalog:
        if piece["status"] == wanted:
            found.append(piece)

    return found


def filter_by_min_price(catalog, min_price):
    """Devuelve las piezas cuyo precio es mayor al precio minimo recibido.

    Lanza ValueError si el precio minimo no es un numero.
    """
    if not isinstance(catalog, list):
        raise ValueError("El catalogo debe ser una lista.")

    if isinstance(min_price, bool) or not isinstance(min_price, (int, float)):
        raise ValueError("El precio minimo debe ser un numero.")

    found = []

    for piece in catalog:
        if piece["price"] > min_price:
            found.append(piece)

    return found


def get_average_price(catalog):
    """Calcula el precio promedio de todas las piezas del catalogo.

    Si el catalogo esta vacio avisa por pantalla y devuelve 0.
    """
    if not isinstance(catalog, list):
        raise ValueError("El catalogo debe ser una lista.")

    try:
        if len(catalog) == 0:
            raise ValueError("El catalogo esta vacio, no se puede calcular el promedio.")

        total = 0

        for piece in catalog:
            total = total + piece["price"]

        return total / len(catalog)

    except ValueError as error:
        print("Error al calcular el promedio: " + str(error))
        return 0
