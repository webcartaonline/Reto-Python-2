"""Funciones de validacion de los datos de una pieza.

Ninguna de estas funciones imprime nada: solo lanzan ValueError
cuando el dato recibido no es correcto.
"""

ALLOWED_STATUSES = ["disponible", "reservada", "vendida"]


def validate_not_empty(value, field_name):
    """Valida que un campo de texto no venga vacio."""
    if value is None:
        raise ValueError("El campo '" + field_name + "' no puede estar vacio.")

    if str(value).strip() == "":
        raise ValueError("El campo '" + field_name + "' no puede estar vacio.")

    return True


def validate_price(price):
    """Valida que el precio sea un numero y que sea mayor que cero."""
    if isinstance(price, bool) or not isinstance(price, (int, float)):
        raise ValueError("El precio debe ser un numero.")

    if price <= 0:
        raise ValueError("El precio debe ser mayor que cero.")

    return True


def validate_status(status):
    """Valida que el estado sea uno de los permitidos."""
    if not isinstance(status, str):
        raise ValueError("El estado debe ser un texto.")

    if status.strip().lower() not in ALLOWED_STATUSES:
        raise ValueError(
            "El estado debe ser uno de estos: " + ", ".join(ALLOWED_STATUSES) + "."
        )

    return True


def validate_description(description):
    """Valida que la descripcion incluya la palabra usada o certificada."""
    if not isinstance(description, str):
        raise ValueError("La descripcion debe ser un texto.")

    texto = description.lower()

    if "usada" not in texto and "certificada" not in texto:
        raise ValueError(
            "La descripcion debe contener la palabra 'usada' o 'certificada'."
        )

    return True
