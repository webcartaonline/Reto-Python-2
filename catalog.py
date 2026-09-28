"""Functions for the collectible pieces catalog.

This module adds, lists, finds, removes and filters pieces, and computes
metrics. Validation is always delegated to the validations module.
"""

import validations


def add_piece(piece_id, name, category, price, status, description):
    """Validate the received data and return the piece as a dictionary."""
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
    """Return a list with the names of all the pieces in the catalog."""
    if not isinstance(catalog, list):
        raise ValueError("The catalog must be a list.")

    names = []

    for piece in catalog:
        names.append(piece["name"])

    return names


def find_piece_by_id(catalog, piece_id):
    """Find a piece by its id and return it, or None if it is not there."""
    if not isinstance(catalog, list):
        raise ValueError("The catalog must be a list.")

    for piece in catalog:
        if piece["id"] == str(piece_id).strip():
            return piece

    return None


def remove_piece(catalog, piece_id):
    """Remove a piece from the catalog by its id.

    Return True if it was removed and False if the piece was not there.
    """
    if not isinstance(catalog, list):
        raise ValueError("The catalog must be a list.")

    try:
        piece = find_piece_by_id(catalog, piece_id)

        if piece is None:
            raise ValueError("The piece with id '" + str(piece_id) + "' was not found.")

        catalog.remove(piece)
        return True

    except ValueError as error:
        print("Error removing the piece: " + str(error))
        return False


def piece_exists(catalog, piece_id):
    """Tell whether a piece is in the catalog, without raising errors."""
    if not isinstance(catalog, list):
        raise ValueError("The catalog must be a list.")

    return find_piece_by_id(catalog, piece_id) is not None


def get_catalog_summary(catalog):
    """Count how many pieces there are in each category.

    Return a dictionary where the key is the category and the value
    is the number of pieces in that category.
    """
    if not isinstance(catalog, list):
        raise ValueError("The catalog must be a list.")

    summary = {}

    for piece in catalog:
        category = piece["category"]

        if category in summary:
            summary[category] = summary[category] + 1
        else:
            summary[category] = 1

    return summary


def get_pieces_by_category(catalog, category):
    """Return the names of the pieces that belong to a category.

    If there are no matches, return an empty list.
    """
    if not isinstance(catalog, list):
        raise ValueError("The catalog must be a list.")

    wanted = str(category).strip().lower()
    names = []

    for piece in catalog:
        if piece["category"].strip().lower() == wanted:
            names.append(piece["name"])

    return names


def filter_by_status(catalog, status):
    """Return the pieces that have the given status.

    Raise ValueError if the status is not one of the allowed ones.
    """
    if not isinstance(catalog, list):
        raise ValueError("The catalog must be a list.")

    validations.validate_status(status)

    wanted = status.strip().lower()
    found = []

    for piece in catalog:
        if piece["status"] == wanted:
            found.append(piece)

    return found


def filter_by_min_price(catalog, min_price):
    """Return the pieces whose price is greater than the given minimum price.

    Raise ValueError if the minimum price is not a number.
    """
    if not isinstance(catalog, list):
        raise ValueError("The catalog must be a list.")

    if isinstance(min_price, bool) or not isinstance(min_price, (int, float)):
        raise ValueError("The minimum price must be a number.")

    found = []

    for piece in catalog:
        if piece["price"] > min_price:
            found.append(piece)

    return found


def get_average_price(catalog):
    """Compute the average price of all the pieces in the catalog.

    If the catalog is empty, print a warning and return 0.
    """
    if not isinstance(catalog, list):
        raise ValueError("The catalog must be a list.")

    try:
        if len(catalog) == 0:
            raise ValueError("The catalog is empty, the average cannot be computed.")

        total = 0

        for piece in catalog:
            total = total + piece["price"]

        return total / len(catalog)

    except ValueError as error:
        print("Error computing the average: " + str(error))
        return 0
