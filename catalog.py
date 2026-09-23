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
